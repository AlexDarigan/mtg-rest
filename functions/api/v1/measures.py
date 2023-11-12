from firebase_admin import initialize_app, firestore
from google.cloud.firestore_v1 import aggregation
from datetime import datetime
from google.cloud.firestore_v1.base_query import FieldFilter, And, Or
import time
import statistics

def _get_color_filters(colors):
    filters = []
    for color in colors:
        match color:
            case "R": filters.append(FieldFilter("red", "==", True))
            case "G": filters.append(FieldFilter("green", "==", True))
            case "U": filters.append(FieldFilter("blue", "==", True))
            case "W": filters.append(FieldFilter("white", "==", True))
            case "B": filters.append(FieldFilter("black", "==", True))
            case "N": filters.append(FieldFilter("colorless", "==", True))
            case "A": 
                for color in ["red", "green", "blue", "white", "black", "colorless"]:
                    filters.append(FieldFilter(color, "==", True))
    return Or(filters=filters)
    
def _get_card_type_filters(cardtypes):
    filters = []
    for card_key in cardtypes:
        match card_key:
            case "C": filters.append(FieldFilter("Creature", "==", True))
            case "A": filters.append(FieldFilter("Artifact", "==", True))
            case "E": filters.append(FieldFilter("Enchantment", "==", True))
            case "I": filters.append(FieldFilter("Instant", "==", True))
            case "S": filters.append(FieldFilter("Sorcery", "==", True))
            case "L": filters.append(FieldFilter("Land", "==", True))
            case "A": 
                for card_type in ["Land", "Creature", "Artifact", "Enchantment", "Sorcery"]:
                    filters.append(FieldFilter(card_type, "==", True))
    return Or(filters=filters)

def get_color_measures(start, end, cardtypes):
    db = firestore.client()
    
    type_filter = _get_card_type_filters(cardtypes=cardtypes)
        
    begin = time.time()
    results = {}
    for color in ["red", "green", "blue", "black", "white", "colorless"]:
        query = (db.collection("cards")
                .where(filter=FieldFilter("released", ">", start))
                .where(filter=FieldFilter("released", "<", end))
                .where(filter=FieldFilter(color, "==", True))
                .where(filter=type_filter)
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
    
    values = list(results.values())
    mode = statistics.mode(values)
    median = statistics.median(values + [0])
    average = statistics.mean(values)
    maximum = max(values)
    minimum = max(values)
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
    
def get_card_type_measures(start, end, colors):
    db = firestore.client()

    color_filters = _get_color_filters(colors)
    
    begin = time.time()
    results = {}
    for card_type in ["Land", "Creature", "Sorcery", "Instant", "Enchantment", "Artifact"]:
        query = (db.collection("cards")
                .where(filter=FieldFilter("released", ">", start))
                .where(filter=FieldFilter("released", "<", end))
                .where(filter=FieldFilter(card_type, "==", True))
                .where(filter=color_filters)
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
    
    values = list(results.values())
    mode = statistics.mode(values)
    median = statistics.median(values + [0])
    average = statistics.mean(values)
    maximum = max(values)
    minimum = max(values)
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