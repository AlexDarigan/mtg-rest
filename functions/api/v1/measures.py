from firebase_admin import initialize_app, firestore
from google.cloud.firestore_v1 import aggregation
from datetime import datetime
from google.cloud.firestore_v1.base_query import FieldFilter, And, Or
import time
import statistics

def calculate(results, reverseIndex):
    values = list(results.values())
    mode = statistics.mode(values)
    median = (sorted(values)[len(values) // 2])
    average = statistics.mean(values)
    maximum = max(values)
    minimum = min(values)
    total = sum(values)

    return {
        "min": reverseIndex[minimum],
        "max": reverseIndex[maximum],
        "mode": reverseIndex[mode],
        "median": reverseIndex[median],
        "average": average,
        "values": results,
        "total": total
    }

def _get_card_type_filters(cardtypes):
    types = []
    for card_key in cardtypes:
        match card_key:
            case "C": types.append("Creature")
            case "A": types.append("Artifact")
            case "E": types.append("Enchantment")
            case "I": types.append("Instant")
            case "S": types.append("Sorcery")
            case "L": types.append("Land")
            case "A": 
                for card_type in ["Land", "Creature", "Artifact", "Enchantment", "Sorcery"]:
                    types.append(card_type)
    return types

def get_color_measures(start, end, cardtypes):
    db = firestore.client()
    
    types = _get_card_type_filters(cardtypes=cardtypes)
        
    begin = time.time()
    results = {}
    for color in ["red", "green", "blue", "black", "white", "colorless"]:
        query = (db.collection("cards")
                .where(filter=FieldFilter("released", ">", start))
                .where(filter=FieldFilter("released", "<", end))
                .where(filter=FieldFilter(color, "==", True))
                .where(filter=FieldFilter("types", "array_contains_any", types))
            )
        results[color] = aggregation.AggregationQuery(query).count().get()[0][0].value

    
    print("took: ", time.time() - begin)
    print(results)
    reverseIndex = {
        results["red"]: "red",
        results["blue"]: "blue",
        results["green"]: "green",
        results["black"]: "black",
        results["white"]: "white",
        results["colorless"]: "colorless",
    }
    
    return calculate(results, reverseIndex)
    
def get_card_type_measures(start, end, colors):
    db = firestore.client()

    colors_filters = []
    if colors == "A":
        colors_filters = ["R", "G", "B", "U", "W", "N"]
    else:
        colors_filters = [*colors]
    print(colors_filters)
    
    begin = time.time()
    results = {}
    for card_type in ["Land", "Creature", "Sorcery", "Instant", "Enchantment", "Artifact"]:
        query = (db.collection("cards")
                .where(filter=FieldFilter("released", ">", start))
                .where(filter=FieldFilter("released", "<", end))
                .where(filter=FieldFilter(card_type, "==", True))
                .where(filter=FieldFilter("colors", "array_contains_any", colors_filters))
        )
        results[card_type] = aggregation.AggregationQuery(query).count().get()[0][0].value

    print("took: ", time.time() - begin)
    reverseIndex = {
        results["Land"]: "Land",
        results["Creature"]: "Creature",
        results["Enchantment"]: "Enchantment",
        results["Instant"]: "Instant",
        results["Sorcery"]: "Sorcery",
        results["Artifact"]: "Artifact",
    }
    
    return calculate(results, reverseIndex)
    
