from firebase_admin import initialize_app, firestore

def get_price_trend(cardname):
    db = firestore.client()
    cards = db.collection("cards").where("name", "==", cardname).get()
    results = []
    for card in cards:
        d = card.to_dict()
        results.append({
                "name": cardname,
                "set_name": d["set_name"],
                "rarity": d["rarity"],
                "prices": d["prices"],
                "img": d["image"]
            }
        )
    return results
