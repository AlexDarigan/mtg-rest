# Measures = Mean/Mode/Median/Max/Min/Sum
from firebase_admin import initialize_app, firestore
from datetime import datetime
from google.cloud.firestore_v1.base_query import FieldFilter, And, Or
import time

# app = initialize_app(options={"projectId": "mtg-rest"})

# # Create a reference to the cities collection
# cities_ref = db.collection("cities")

# # Create a query against the collection
# query_ref = cities_ref.where(filter=FieldFilter("state", "==", "CA"))

# from google.cloud import firestore
# from google.cloud.firestore_v1.base_query import FieldFilter, Or


# def query_or_composite_filter(project_id: str) -> None:
#     # Instantiate the Firestore client
#     client = firestore.Client(project=project_id)
#     col_ref = client.collection("users")

#     filter_1 = FieldFilter("birthYear", "==", 1906)
#     filter_2 = FieldFilter("birthYear", "==", 1912)

#     # Create the union filter of the two filters (queries)
#     or_filter = Or(filters=[filter_1, filter_2])

#     # Execute the query
#     docs = col_ref.where(filter=or_filter).stream()

#     print("Documents found:")
#     for doc in docs:
#         print(f"ID: {doc.id}")

def get_color_measures(dao, start, end, cardtype, min_cost = 1, max_cost = 20):
    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)
    db = firestore.client()
    collection = db.collection("cards")
    
    f1 = FieldFilter("released", ">", start)
    f2 = FieldFilter("released", "<", end)
    cost_filters = []
    for cost in range(min_cost, max_cost):
        cost_filters.append(FieldFilter("cmc", "==", cost))
    or_filter = Or(filters=cost_filters)
    query = (collection.where(filter=f1).where(filter=f2)) #.where(filter=or_filter))
     
    start = time.time()
    for doc in query.stream():
        print(f"{doc.id} -> {doc.to_dict().get('cmc')}")
        
    took = time.time()
    return took

def get_card_type_measures(start, end, color, cost):
    # get cards within_range & cost = ? & get(color) == True (colors are seperated currently?)
    pass

def get_cost_measures(start, end, color, type):
    pass


# calculations
# max()
# mean()
# min()
# sum()
# median()
# average()