# Measures = Mean/Mode/Median/Max/Min/Sum
from firebase_admin import initialize_app, firestore
from google.cloud.firestore_v1 import aggregation
from datetime import datetime
from google.cloud.firestore_v1.base_query import FieldFilter, And, Or
import time
import statistics

def get_color_measures(dao, start, end, cardtype, min_cost = 1, max_cost = 20):
    
    # put some of these into dao   
    db = firestore.client()
    
    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)
    db = firestore.client()
       
    
    redQ = (db.collection("cards")
             .where(filter=FieldFilter("released", ">", start))
             .where(filter=FieldFilter("released", "<", end))
             .where(filter=FieldFilter("red", "==", True))
             .where(filter=_get_cost_filters(min_cost, max_cost))
            )
    
    blueQ = (db.collection("cards")
             .where(filter=FieldFilter("released", ">", start))
             .where(filter=FieldFilter("released", "<", end))
             .where(filter=FieldFilter("blue", "==", True))
             .where(filter=_get_cost_filters(min_cost, max_cost))
            )
    
    blackQ = (db.collection("cards")
             .where(filter=FieldFilter("released", ">", start))
             .where(filter=FieldFilter("released", "<", end))
             .where(filter=FieldFilter("black", "==", True))
             .where(filter=_get_cost_filters(min_cost, max_cost))
            )
    
    greenQ = (db.collection("cards")
             .where(filter=FieldFilter("released", ">", start))
             .where(filter=FieldFilter("released", "<", end))
             .where(filter=FieldFilter("green", "==", True))
             .where(filter=_get_cost_filters(min_cost, max_cost))
            )
    
    whiteQ = (db.collection("cards")
             .where(filter=FieldFilter("released", ">", start))
             .where(filter=FieldFilter("released", "<", end))
             .where(filter=FieldFilter("white", "==", True))
             .where(filter=_get_cost_filters(min_cost, max_cost))
            )
    
    colorlessQ = (db.collection("cards")
             .where(filter=FieldFilter("released", ">", start))
             .where(filter=FieldFilter("released", "<", end))
             .where(filter=FieldFilter("colorless", "==", True))
             .where(filter=_get_cost_filters(min_cost, max_cost))
            )
     
    start = time.time()
    redC = aggregation.AggregationQuery(redQ).count().get()
    blueC = aggregation.AggregationQuery(blueQ).count().get()
    blackC = aggregation.AggregationQuery(blackQ).count().get()
    greenC = aggregation.AggregationQuery(greenQ).count().get()
    whiteC = aggregation.AggregationQuery(whiteQ).count().get()
    colorlessC = aggregation.AggregationQuery(colorlessQ).count().get()
    
    redT = redC[0][0].value
    blueT = blueC[0][0].value
    blackT = blackC[0][0].value
    greenT = greenC[0][0].value
    whiteT = whiteC[0][0].value
    colorlessT = colorlessC[0][0].value
    
    values = [redT, blueT, blackT, greenT, whiteT, colorlessT]
    average = statistics.mean(values)
    mode = statistics.mode(values)
    median = statistics.median(values)
    took = time.time() - start
    print("took: ", took)
    # need to get keys too, lol.
    print(average, mode, median)
    return str({"median": median, "mode": mode, "average": average})

def _get_cost_filters(min, max):
    filters = []
    for cost in range(min, max):
        filters.append(FieldFilter("cmc", "==", cost))
    return Or(filters=filters)

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