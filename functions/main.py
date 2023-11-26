from firebase_admin import initialize_app
from firebase_functions import options, scheduler_fn, https_fn, pubsub_fn
from services import gatherer, preprocessor, publisher, dao, bigquerydao, bq_preprocessor
from api.v1 import measures, trends, cards
from concurrent.futures import wait
from datetime import datetime
import json

# Initialization
options.set_global_options(max_instances=1, memory=options.MemoryOption.GB_4, cpu=2, timeout_sec=540)
initialize_app()

# v1/color/distribution
@https_fn.on_request()
def get_color_distribution(request):
    # x = datetime.fromisoformat("20230101").date().isoformat()
    start = datetime.fromisoformat(request.args.get("start", "20030101")).date().isoformat()
    end = datetime.fromisoformat(request.args.get("end", datetime.now().isoformat())).date().isoformat()
    result = measures.get_color_measures(start=start, end=end)
    return json.dumps(result)

# v1/card
@https_fn.on_request()
def get_card(request):
    cardname = request.args.get("name")
    result = cards.get_card(cardname)
    return json.dumps(result)
    
# v1/price/trend?=name
@https_fn.on_request()
def get_price_trends(request):
    cardname = request.args.get("name")
    start = datetime.fromisoformat(request.args.get("start", "20030101")).date().isoformat()
    end = datetime.fromisoformat(request.args.get("end", datetime.now().isoformat())).date().isoformat()
    result = trends.get_price_trend(card=cardname, start=start, end=end)
    return json.dumps(result)

@scheduler_fn.on_schedule(schedule="0 3 * * *")
def update_big_query(event):
    cards, prices = bq_preprocessor.transform(gatherer.fetch_cards("https://api.scryfall.com/bulk-data/default-cards"))
    bigquerydao.update_cards(cards)
    bigquerydao.update_prices(prices)
