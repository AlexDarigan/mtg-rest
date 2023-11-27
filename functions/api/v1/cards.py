from google.cloud import bigquery

def get_card(card):
    client = bigquery.Client("mtg-rest")
    query = f"""
    SELECT * FROM `mtg-rest.mtgcards.cards` WHERE name = {card}
    """
    
    execution = client.query(query)
    try:
        found = []
        result = execution.result()
        for row in result:
            found.append({"id": row.id, "name": row.name, "rarity": row.rarity, "image": row.image, "set": row.set_name})
        return found
    except:
        print("errors")
        print(execution.errors)
    return {}