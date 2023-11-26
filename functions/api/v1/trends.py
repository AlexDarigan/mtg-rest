from firebase_admin import initialize_app, firestore
from google.cloud import bigquery
from datetime import datetime
from statistics import mean, median, mode

def get_price_trend(card, start, end):
    client = bigquery.Client("mtg-rest")
    query = f"""
    SELECT cards.name, cards.id, cards.image, cards.rarity, prices.date, prices.eur, prices.usd
    FROM `mtg-rest.mtgcards.cards` AS cards
    JOIN `mtg-rest.mtgcards.prices` AS prices ON cards.id = prices.id
    WHERE cards.name = "{card}" 
    AND date > PARSE_DATE("%F", "{start}")
    AND date < PARSE_DATE("%F", "{end}")
    """
    execution = client.query(query)
    try:
        records = {}
        result = execution.result()
        for row in result:
            record = records.get(row.id, {"image": row.image, "rarity": row.rarity, "prices": []})
            record["prices"].append({str(row.date): {"eur": row.eur, "usd": row.usd}})
            records[row.id] = record
        return records
    except:
        print("errors")
        print(execution.errors)
    return []
