from google.cloud import bigquery

def get_price_trend(card_id, start, end):
    client = bigquery.Client("mtg-rest")
    query = f"""
    SELECT cards.name, cards.id, prices.date, prices.eur, prices.usd
    FROM `mtg-rest.mtgcards.cards` AS cards
    JOIN `mtg-rest.mtgcards.prices` AS prices ON cards.id = prices.id
    WHERE cards.id = {card_id} 
    AND date > PARSE_DATE("%F", "{start}")
    AND date < PARSE_DATE("%F", "{end}")
    """
    execution = client.query(query)
    try:
        records = []
        result = execution.result()
        for row in result:
            records.append({"date": str(row.date), "eur": row.eur, "usd": row.usd})
        return records
    except:
        print("errors")
        print(execution.errors)
    return []