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
    
def _get_card_type_filters(cardtypes):
    filters = []
    for card_key in cardtypes:
        match card_key:
            case "C": filters.append("Creature")
            case "A": filters.append("Artifact")
            case "E": filters.append("Enchantment")
            case "I": filters.append("Instant")
            case "S": filters.append("Sorcery")
            case "L": filters.append("Land")
            case "A": filters = ["Land", "Creature", "Artifact", "Enchantment", "Sorcery", "Land"]
    return filters

def get_color_measures(start, end, cardtypes):
    db = firestore.client()
    
    begin = time.time()
    results = {}
    for color in ["red", "green", "blue", "black", "white", "colorless"]:
        query = (db.collection("cards")
                .where(filter=FieldFilter("released", ">", start))
                .where(filter=FieldFilter("released", "<", end))
                .where(filter=FieldFilter(color, "==", True))
                .where(filter=FieldFilter("types", "array_contains_any", ["Creature", "Land", "Artifact", "Enchantment", "Sorcery", "Instant"]))
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
    
    values = results.values()
    mode = statistics.mode(values)
    median = statistics.median(values + [0])
    average = statistics.mean(values)
    maximum = max(results.values)
    minimum = max(results.values)
    total = sum(results.values)

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

    red, green, blue, white, black, colorless = _get_color_booleans(colors)
    
    begin = time.time()
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
    
    values = results.values()
    mode = statistics.mode(values)
    median = statistics.median(values + [0])
    average = statistics.mean(values)
    maximum = max(results.values)
    minimum = max(results.values)
    total = sum(results.values)

    return {
        "min": reverseIndex[minimum],
        "max": reverseIndex[maximum],
        "mode": reverseIndex[mode],
        "median": reverseIndex[median],
        "average": average,
        "values": results,
        "total": total
    }