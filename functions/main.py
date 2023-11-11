from firebase_admin import initialize_app
from firebase_functions import options, scheduler_fn, https_fn, pubsub_fn
from services import gatherer, preprocessor, publisher, dao #, Service: DataExplorer (? <--- ) / API thing
from concurrent.futures import wait
from datetime import datetime

# Initialization
options.set_global_options(max_instances=1, memory=options.MemoryOption.GB_4, cpu=2, timeout_sec=540)
initialize_app()

# API Calls

# Measures
@https_fn.on_request()
def get_measure(request):
    return "Measures not implemented"

# Price Trends
@https_fn.on_request()
def get_price_trend(request):
    return "Trends not implemented"

# Scheduled Function for data processing
@scheduler_fn.on_schedule(schedule="0 3 * * *")
def publish_cards(event):
    run = dao.begin_run()
    data = gatherer.fetch_cards("https://api.scryfall.com/bulk-data/default-cards")
    cards = preprocessor.transform(data)
    wait(publisher.publish(run.id, cards)) 
    dao.end_run(run)
        
@pubsub_fn.on_message_published(topic="cards")
def on_cards_published(event):
    data = event.data.message.json
    chunk = dao.begin_run_chunk(data)
    dao.add_card_batch(data["chunk"])
    dao.end_run_chunk(chunk)

