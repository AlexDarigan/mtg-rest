from firebase_admin import initialize_app
from firebase_functions import options, scheduler_fn, https_fn, pubsub_fn
from services import gatherer, preprocessor, publisher, dao, bigquerydao, bq_preprocessor
from api.v1 import measures, trends
from concurrent.futures import wait
from datetime import datetime
import json

# Initialization
options.set_global_options(max_instances=1, memory=options.MemoryOption.GB_4, cpu=2, timeout_sec=540)
initialize_app()

# API Calls
# v1/measure/color?start=?&end=?&card_types=?
@https_fn.on_request()
def get_color_measures(request):
    start = datetime.fromisoformat(request.args.get("start", "19930805")) # August 5th 1993 - When MTG was released
    end = datetime.fromisoformat(request.args.get("end", datetime.now().isoformat()))
    cardtypes = request.args.get("types", "A").upper()
    result = measures.get_color_measures(start=start, end=end, cardtypes=cardtypes)
    return json.dumps(result)

# v1/measure/color?start=?&end=?&colors=?
@https_fn.on_request()
def get_card_type_measures(request):
    start = datetime.fromisoformat(request.args.get("start", "19930805")) # August 5th 1993 - When MTG was released
    end = datetime.fromisoformat(request.args.get("end", datetime.now().isoformat()))
    colors = request.args.get("colors", "A").upper()
    result = measures.get_card_type_measures(start=start, end=end, colors=colors)
    return json.dumps(result)
    
# v1/price/trends?=name
@https_fn.on_request()
def get_price_trends(request):
    cardname = request.args.get("name")
    result = trends.get_price_trend(cardname)
    return json.dumps(result)

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


@scheduler_fn.on_schedule(schedule="0 3 * * *")
def update_big_query(event):
    cards, prices = bq_preprocessor.transform(gatherer.fetch_cards("https://api.scryfall.com/bulk-data/default-cards"))
    bigquerydao.update_cards(cards)
    bigquerydao.update_prices(prices)
