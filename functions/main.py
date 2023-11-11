from firebase_functions import https_fn
from firebase_admin import initialize_app

# initialize_app()
#
#
# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")


# Service: Gatherer
# Service: Preprocessor
# Service: Publisher
# Service: Firestore
# Service: DataExplorer (? <--- ) / API thing

# process()
# publish()

# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from concurrent.futures import wait
from datetime import datetime
from firebase_functions import options, scheduler_fn, https_fn, pubsub_fn
from firebase_admin import initialize_app, firestore
import time

from services import gatherer, preprocessor, publisher, dao

# TODO
# Split into Routes, Services & Utils
options.set_global_options(max_instances=1, memory=options.MemoryOption.GB_4, cpu=2, timeout_sec=540)

initialize_app()

# Measures
@https_fn.on_request()
def get_measure(request: https_fn.Request) -> https_fn.Response:
    return "Measures not implemented"

# Price Trends
@https_fn.on_request()
def get_price_trend(request: https_fn.Request) -> https_fn.Response:
    return "Trends not implemented"


@scheduler_fn.on_schedule(schedule="0 3 * * *")
def publish_cards(event):
    # get client
    db = firestore.client()
    
    # addRun()
    _, run = db.collection("run").add({"start": firestore.SERVER_TIMESTAMP})
        
    data = gatherer.fetch_cards("https://api.scryfall.com/bulk-data/default-cards")
    cards = preprocessor.transform(data)
    wait(publisher.publish(run.id, cards))
    
    run.update({"end": firestore.SERVER_TIMESTAMP})
    print("end -> ", datetime.now(), flush=True)
        
@pubsub_fn.on_message_published(topic="cards")
def on_cards_published(event: pubsub_fn.CloudEvent[pubsub_fn.MessagePublishedData]):
    
    start = time.time()
    data = event.data.message.json
    db = firestore.client()
        
    print(f'{datetime.now()}: Adding Count {data["count"]}')
    
    _, chunk = (db.collection("run")
                    .document(data["runId"])
                    .collection("chunks")
                    .add({
                        "start": firestore.SERVER_TIMESTAMP, 
                        "chunkId": data["count"], 
                        "batch_count": data["batch_count"]
                    }))
    

    cards = db.collection("cards")
    batch = db.batch()
    for doc in data["chunk"]:
        card = cards.document(doc["id"])
        
        # Convert json string back to timestamp
        doc["released"] = datetime.fromisoformat(doc["released"])
        print("RELEASED", doc["released"])

        batch.set(card, doc, merge=True)
    batch.commit()

    print(f'{datetime.now()} Added Count {data["count"]}')
    
    end = time.time()
    chunk.update({"end": firestore.SERVER_TIMESTAMP, "took": end - start})


