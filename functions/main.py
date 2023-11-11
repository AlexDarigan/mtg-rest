from firebase_admin import initialize_app
from firebase_functions import options, scheduler_fn, https_fn, pubsub_fn
from services import gatherer, preprocessor, publisher, dao #, Service: DataExplorer (? <--- ) / API thing
from api.v1 import measures, trends
from concurrent.futures import wait
from datetime import datetime


# Initialization
options.set_global_options(max_instances=1, memory=options.MemoryOption.GB_4, cpu=2, timeout_sec=540)
initialize_app()

# API Calls

# Measures
#@https_fn.on_request()
# def get_measure(request):
#     YYYY_MM_DD = "%Y%m%d"
#     YYYY_MM_DD = "%Y%m%d"
#     start = request.args.get("start", "20231103")
#     end = request.args.get("end", datetime.now().strftime(YYYY_MM_DD))
#     measures = request.args.get("of")
#     cost = request.args("cmc")
#     card_type = request.args("card_type")
#     return measures.get_mean(
#         start = start, end = end, 
#         of="color", cmc= -1, card_type = )

# mode/median/mean max/min/sum    

# We can 
# v1/measure/color?start=?&end=?&cost=?&card_type=?
@https_fn.on_request()
def get_color_measures(request):
    start = "19940101"
    end = "20231111"
    return measures.get_color_measures(
        dao=dao, 
        start=start, end=end,
        min_cost=0, max_cost=16,
        cardtype="any")
    

# # v1/measure/card_type?start=?&end=?&cost=?&color=?
# @https_fn.on_request()
# def get_card_type_measures(request):
#     return "Card Type Measures"

# # v1/measure/cost?start=?&end=?&color=?&card_type=?
# @https_fn.on_request()
# def get_cost_measures(request):
#     return "Cost Measures"


# # Price Trends
# @https_fn.on_request()
# def get_price_trend(request):
#     return "Trends not implemented"

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

