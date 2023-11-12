# Measures = Mean/Mode/Median/Max/Min/Sum
from firebase_admin import initialize_app, firestore
from google.cloud.firestore_v1 import aggregation
from datetime import datetime
from google.cloud.firestore_v1.base_query import FieldFilter, And, Or
import time
import statistics

def _get_color_booleans(colors):
    if "A" in colors:
        return(True, True, True, True, True, True)
    else:
        return ("R" in colors, "G" in colors, "U" in colors, "W" in colors, "B" in colors, "N" in colors)
    
def _get_type_booleans(types):
    if "A" in types:
        return (True, True, True, True, True, True)
    else:
        return ("L" in types, "C" in types, "S" in types, "I" in types, "E" in types, "A" in types)

def _get_cost_filters(min, max):
    filters = []
    for cost in range(min, max):
        filters.append(FieldFilter("cmc", "==", cost))
    return Or(filters=filters)

def get_color_measures(dao, start, end, cardtype, min_cost = 1, max_cost = 16):
    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)
    db = firestore.client()
    
    cost_filters = _get_cost_filters(min_cost, max_cost)
    land, creature, sorcery, instant, enchantment, artifact = _get_type_booleans(cardtype)
        
    starttime = time.time()
    results = {}
    for color in ["red", "green", "blue", "black", "white", "colorless"]:
        query = (db.collection("cards")
                .where(filter=FieldFilter("released", ">", start))
                .where(filter=FieldFilter("released", "<", end))
                .where(filter=FieldFilter(color, "==", True))
                .where(filter=FieldFilter("Land", "==", land))
                .where(filter=FieldFilter("Creature", "==", creature))
                .where(filter=FieldFilter("Artifact", "==", sorcery))
                .where(filter=FieldFilter("Enchantment", "==", sorcery))
                .where(filter=FieldFilter("Instant", "==", instant))
                .where(filter=FieldFilter("Sorcery", "==", sorcery))
                .where(filter=cost_filters)
            )
        retval = aggregation.AggregationQuery(query).count().get()
        results[color] = retval[0][0].value
    
    print("took: ", time.time() - starttime)
    
    
    # values = [redT, blueT, blackT, greenT, whiteT, colorlessT]
    # average = statistics.mean(values)
    # mode = statistics.mode(values)
    # median = statistics.median(values)
    # took = time.time() - start
    # print("took: ", took)
    # # need to get keys too, lol.
    # print(average, mode, median)
    # return str({"median": median, "mode": mode, "average": average})

def get_card_type_measures(start, end, colors = "A", min_cost = 1, max_cost = 20):
    # get cards within_range & cost = ? & get(color) == True (colors are seperated currently?)
    
    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)
    
    red, green, blue, white, black, colorless = _get_color_booleans(colors)
    cost_filters = _get_cost_filters(min_cost, max_cost)

    start = time.time()
    db = firestore.client()
    results = {}
    for card_type in ["Land", "Creature", "Sorcery", "Instant", "Enchantment", "Artifact"]:
        query = (db.collection("cards")
                .where(filter=FieldFilter("released", ">", start))
                .where(filter=FieldFilter("released", "<", end))
                .where(filter=FieldFilter(card_type, "==", True))
                .where(filter=FieldFilter("Red", "==", red))
                .where(filter=FieldFilter("Blue", "==", blue))
                .where(filter=FieldFilter("Green", "==", green))
                .where(filter=FieldFilter("Black", "==", black))
                .where(filter=FieldFilter("White", "==", white))
                .where(filter=FieldFilter("Colorless", "==", colorless))
                .where(filter=cost_filters))
        retval = aggregation.AggregationQuery(query).count().get()
        results[card_type] = retval[0][0].value
    print("took: ", time.time() - start)
    return results
    

def get_cost_measures(start, end, color, type):
    pass


# calculations
# max()
# mean()
# min()
# sum()
# median()
# average()