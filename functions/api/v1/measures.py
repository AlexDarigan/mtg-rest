from google.cloud import bigquery
from datetime import datetime
from statistics import mean, median, mode

def get_color_count(color, start, end):
    client = bigquery.Client("mtg-rest")
    query = f"""
        SELECT COUNT(colors) 
        FROM `mtg-rest.mtgcards.cards`  
        WHERE 
        released > PARSE_DATE("%F", "{start}") 
        AND released < PARSE_DATE("%F", "{end}")
        AND "{color}" IN UNNEST(colors)
    """
    execution = client.query(query)
    try:
        result = execution.result(max_results=1)
        count = list(result)[0][0]
        return count
    except:
        print(execution.errors)
    return 0
    
   

def get_colorless_count(start, end):
    client = bigquery.Client("mtg-rest")
    query = f"""
        SELECT COUNT(colors) 
        FROM `mtg-rest.mtgcards.cards`  
        WHERE 
        released > PARSE_DATE("%F", "{start}") 
        AND released < PARSE_DATE("%F", "{end}")
        AND ARRAY_LENGTH(colors) = 0
    """
    execution = client.query(query)
    try:
        result = execution.result(max_results=1)
        count = list(result)[0][0]
        return count
    except:
        print(execution.errors)
    return 0
    

def get_color_measures(start, end):
    colors = {
        "R": get_color_count("R", start, end),
        "G": get_color_count("G", start, end),
        "B": get_color_count("B", start, end),
        "U": get_color_count("U", start, end),
        "W": get_color_count("W", start, end),
        "N": get_colorless_count(start, end)
    }
    
    return colors