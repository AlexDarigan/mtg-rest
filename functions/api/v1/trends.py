from firebase_admin import initialize_app, firestore

def get_price_trend(cardname):
    db = firestore.client()
    cards = db.collection("cards").where("name", "==", cardname).stream()
    results = []
    for card in cards:
        print(cards)
        d = card.to_dict()
        results.append({
                "name": cardname,
                "set_name": d["set_name"],
                "prices": d["prices"],
                "img": d["image"],
            }
        )
    return results
