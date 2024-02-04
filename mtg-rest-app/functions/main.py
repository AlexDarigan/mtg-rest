from firebase_admin import initialize_app
from firebase_functions import options, scheduler_fn, https_fn
from services import gatherer, preprocessor, dao
from api.v1 import measures, trends, cards
from datetime import datetime
import json

# Initialization
options.set_global_options(max_instances=1, memory=options.MemoryOption.GB_4, cpu=2, timeout_sec=540)
initialize_app()

# v1/color/distribution
@https_fn.on_request()
def get_color_distribution(request):
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
    
# v1/price/trend?id=g9r
@https_fn.on_request()
def get_price_trends(request):
    card_id = request.args.get("id")
    start = datetime.fromisoformat(request.args.get("start", "20030101")).date().isoformat()
    end = datetime.fromisoformat(request.args.get("end", datetime.now().isoformat())).date().isoformat()
    result = trends.get_price_trend(card_id=card_id, start=start, end=end)
    return json.dumps(result)

@scheduler_fn.on_schedule(schedule="0 3 * * *")
def update_big_query(event):
    cards, prices = preprocessor.transform(gatherer.fetch_cards("https://api.scryfall.com/bulk-data/default-cards"))
    dao.update_cards(cards)
    dao.update_prices(prices)
