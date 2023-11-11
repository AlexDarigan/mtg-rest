# Service: DataExplorer (? <--- ) / API thing

# process()
# publish()

# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from concurrent.futures import wait
from datetime import datetime
from firebase_functions import options, scheduler_fn, https_fn, pubsub_fn
from firebase_admin import initialize_app
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
    run = dao.begin_run()
    data = gatherer.fetch_cards("https://api.scryfall.com/bulk-data/default-cards")
    cards = preprocessor.transform(data)
    wait(publisher.publish(run.id, cards)) 
    dao.end_run(run)
    print("end -> ", datetime.now(), flush=True)
        
@pubsub_fn.on_message_published(topic="cards")
def on_cards_published(event: pubsub_fn.CloudEvent[pubsub_fn.MessagePublishedData]):
    data = event.data.message.json
    print(f'{datetime.now()}: Adding Count {data["count"]}')
    chunk = dao.begin_run_chunk(data)
    dao.add_card_batch(data["chunked"])
    dao.end_run_chunk(chunk)
    print(f'{datetime.now()} Added Count {data["count"]}')


