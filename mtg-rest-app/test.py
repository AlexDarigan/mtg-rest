from functions.services import dao
from functions.api.v1 import measures, trends
from firebase_admin import initialize_app
from datetime import datetime
import json 

app = initialize_app(options={"projectId": "mtg-rest"})
print(trends.get_price_trend(cardname="Black Lotus"))
# r = measures.get_color_measures(
#     start=datetime.fromisoformat("19930805"), 
#     end=datetime.fromisoformat("20231112"), 
#     cardtypes="A")
# print(json.dumps(r).encode("utf8"))

# x = measures.get_card_type_measures( 
#     start=datetime.fromisoformat("19940101"), 
#     end=datetime.fromisoformat("20231111"), 
#     colors="B")
# print(x)

# # Create a reference to the cities collection
# cities_ref = db.collection("cities")

# # Create a query against the collection
# query_ref = cities_ref.where(filter=FieldFilter("state", "==", "CA"))

# def get_color_measures(dao, start, end, cardtype, min_cost = 1, max_cost = 20):
#     cards = dao.get_cards_released_between(start, end)
#     for card in cards:
#         print(card.id)