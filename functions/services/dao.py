import time
from datetime import datetime
from firebase_admin import initialize_app, firestore

def begin_run():
    db = firestore.client()
    _, run = db.collection("run").add({"start": firestore.SERVER_TIMESTAMP})
    return run

def end_run(run):
    #db = firestore.client()
    run.update({"end": firestore.SERVER_TIMESTAMP})

def begin_run_chunk(chunked):
    db = firestore.client()
    _, chunk = (db.collection("run")
                    .document(chunked["runId"])
                    .collection("chunks")
                    .add({
                        "start": firestore.SERVER_TIMESTAMP, 
                        "chunkId": chunked["count"], 
                        "batch_count": chunked["batch_count"],
                        "start": time.time()
                    }))

def end_run_chunk(chunk):
    chunk.update({"end": firestore.SERVER_TIMESTAMP, "took": time.time() - chunk["start"]})

def add_card_batch(chunked):
    db = firestore.client()
    cards = db.collection("cards")
    
    batch = db.batch()
    for doc in chunked:
        card = cards.document(doc["id"])
        
        # Convert json string back to timestamp
        doc["released"] = datetime.fromisoformat(doc["released"])

        batch.set(card, doc, merge=True)
    batch.commit()