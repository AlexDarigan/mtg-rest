from functions.services import dao
from functions.api.v1 import measures



measures.get_color_measures(
    dao=dao, 
    start="19940101", 
    end="20231111", 
    min_cost=3,
    max_cost=10,
    cardtype="any")

# # Create a reference to the cities collection
# cities_ref = db.collection("cities")

# # Create a query against the collection
# query_ref = cities_ref.where(filter=FieldFilter("state", "==", "CA"))

# def get_color_measures(dao, start, end, cardtype, min_cost = 1, max_cost = 20):
#     cards = dao.get_cards_released_between(start, end)
#     for card in cards:
#         print(card.id)