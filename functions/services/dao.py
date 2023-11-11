import time
from datetime import datetime
from firebase_admin import initialize_app, firestore
from google.cloud.firestore_v1.base_query import FieldFilter, And


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
    return chunk

def end_run_chunk(chunk):
    chunk.update({"end": firestore.SERVER_TIMESTAMP, "took": time.time() - chunk.get().to_dict()["start"]})

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
    
def get_cards_released_between(start, end):
    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)
    db = firestore.client()
    query = (db.collection("cards")
     .where(filter=FieldFilter("released", ">", start))
     .where(filter=FieldFilter("released", "<", end))
     .stream())
    start = time.time()
    for doc in query:
        print(doc.id)
    print(query)
    print("TOOK: ", time.time() - start)
    return query