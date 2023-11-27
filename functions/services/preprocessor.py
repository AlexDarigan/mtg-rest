import pandas as pd
import requests
from datetime import datetime


def get_legal_formats(legalities):
    # There about 30+ different game format in Magic: The Gathering, 
    # ..however only standard, modern and commander significantly affect card prices
    retval = []
    for format in ["standard", "modern", "commander"]:
        if legalities[format] == "legal":
            retval.append(format)
    return retval

def extract_types(type_line, secondary):
    # Splitting the primary card types (land, creature, artifact, enchantment, sorcery, instant)..
    # ..from the secondary card types (saga, human, elf, dragon etc)
    types = type_line.split(" ")
    extracted = []
    if secondary:
        # Searching for secondary card types
        types.reverse()
    for t in types:
        if len(t) == 1:
            return extracted # Found "-"
        extracted.append(t)
    if secondary:
        # If we found no seperator while searching secondary types,
        # ..then there is no secondary types
        return []
    return extracted

def transform(data):

    # Creating our initial data
    df = pd.DataFrame(data)

    # Dropping digital-only cards because digital scarcity can cause problems
    df = df[df.games.apply(lambda games: "paper" in games)]
    
    # Dropping any cards released before 2003 (when modern become codified)
    df = df[df.released_at.apply(lambda release: datetime.fromisoformat(release).year >= 2003)]
    
    # Dropping Double-Faced Cards
    df = df[df.name.apply(lambda x: "//" not in x)]
    
    # Dropping "Un" Joke Sets
    df = df[df.set_name.apply(lambda set_name: not set_name.startswith("Un"))]
    
    # Dropping Basic Lands && Tokens
    df = df[df.type_line.apply(lambda type_line: "Basic Land" not in type_line and "Token" not in type_line)]
    
    df["legalities"] = df["legalities"].apply(get_legal_formats)
    
    # Dropping any card which is not legal in any format
    # We'll hit a few outliers here where the card *was* legal but banned since but we'll hit a lot more
    # of special edition or alt format cards that were never legal
    df = df[df["legalities"].apply(lambda legality: len(legality) != 0)]
    
    # Dropping promotional cards
    df = df[df["promo"].apply(lambda promo: not promo)]

    # Dropping reprints    
    df = df[df["reprint"].apply(lambda reprint: not reprint)]
    
    # Dropping reserved cards
    df = df[df["reserved"].apply(lambda reserved: not reserved)]
    
    # Dropping special variants
    df = df[df["variation"].apply(lambda variation: not variation)]
    
    # Dropping oversized cards
    df = df[df["oversized"].apply(lambda oversized: not oversized)]
    
    # Simple Conversions
    df["released"] = pd.to_datetime(df["released_at"], errors='coerce').astype(str)
    df["cmc"] = pd.to_numeric(df["cmc"], errors='coerce').fillna(0)

    df["primary"] = df["type_line"].apply(lambda x: extract_types(x, secondary=False))
    df["secondary"] = df["type_line"].apply(lambda x: extract_types(x, secondary=True))    
    
    # get prices & date
    df["date"] = str(datetime.today().date())
    df["eur"] = df["prices"].apply(lambda x: dict(x).get("eur"))
    df["usd"] = df["prices"].apply(lambda x: dict(x).get("usd"))
    df["eur"] = pd.to_numeric(df["eur"], errors="coerce").fillna(0.0)
    df["usd"] = pd.to_numeric(df["usd"], errors="coerce").fillna(0.0)
    
    
    df["image"] = df["image_uris"].apply(lambda x: dict(x).get("png"))

    # Creating cards json
    cards_df = pd.DataFrame(data=df, columns=["id", "name", "released", "uri", "cmc", "colors", "primary", "secondary",
                                            "keywords", "legalities", "set_id", "rarity", "set_name", "image",
                                            ])
    cards = cards_df.to_dict(orient="records")
    for card in cards:
        card["cmc"] = int(card["cmc"])
        
    # Creating prices json    
    prices_df = pd.DataFrame(data=df, columns=["id", "date", "eur", "usd"])
    prices = prices_df.to_dict(orient="records")
    return (cards, prices)