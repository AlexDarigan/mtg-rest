from google.cloud import bigquery
from datetime import datetime

# get stats / measures
# get price trends
# price predictions?

# primary, secondary, color, cmc, date
def get_measures(primary, secondary, min_cost, max_cost, start, end):
    # SELECT * FROM TABLE
    # WHERE
    #   primary is any []
    #   AND secondary is any []
    #   AND color is any []
    #   AND cmc is >= min_cost
    #   AND cmc is <= max_cost
    #   AND released => start
    #   AND released <= end 
    pass 

# Primary Measures
# Secondary Measures
# Color Measures
# Cost Measures

# SELECT AVG(cmc) AS avg_cmc
# FROM `project.dataset.magic_cards`;

# count(colors, start, end)


def get_average(measure, start, end):
    client = bigquery.Client("mtg-rest")
    query = f"SELECT AVG({measure}) FROM mtgcards.cards WHERE released > {start} AND released < {end}"

def update_cards(cards):
    client = bigquery.Client("mtg-rest")
    config = bigquery.LoadJobConfig(
        schema = [
            bigquery.SchemaField("id", "STRING", "REQUIRED"),
            bigquery.SchemaField("name", "STRING", "REQUIRED"),
            bigquery.SchemaField("uri", "STRING"),
            bigquery.SchemaField("cmc", "INTEGER"),
            bigquery.SchemaField("colors", "STRING", "REPEATED"),
            bigquery.SchemaField("primary", "STRING", "REPEATED"),
            bigquery.SchemaField("secondary", "STRING", "REPEATED"),
            bigquery.SchemaField("keywords", "STRING", "REPEATED"),
            bigquery.SchemaField("legalities", "STRING", "REPEATED"),
            bigquery.SchemaField("set_id", "STRING"),
            bigquery.SchemaField("set_name", "STRING"),
            bigquery.SchemaField("image", "STRING"),
            bigquery.SchemaField("rarity", "STRING"),
            bigquery.SchemaField("released", "DATE")
        ],
        autodetect=False,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
)

    job = client.load_table_from_json(json_rows=cards, destination="mtgcards.cards", project="mtg-rest", job_config=config)
    try:
        result = job.result()
    except:
        print(job.errors)

def update_prices(prices):
    
    # ADD TO DAILY PRICES
    client = bigquery.Client(project="mtg-rest")
    config = bigquery.LoadJobConfig(
        schema = [
            bigquery.SchemaField("id", "STRING", "REQUIRED"),
            bigquery.SchemaField("date", "DATE", "REQUIRED"),
            bigquery.SchemaField("eur", "FLOAT", "REQUIRED"),
            bigquery.SchemaField("usd", "FLOAT", "REQUIRED")
        ],
        autodetect=False,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
)

    job = client.load_table_from_json(json_rows=prices, destination="mtgcards.daily_prices", project="mtg-rest", job_config=config)
    try:
        result = job.result()
    except:
        print(job.errors)
        
    # Merge With All Prices
    config = bigquery.QueryJobConfig(
        default_dataset="mtg-rest.mtgcards",
)

    merge_job = f"""
        MERGE INTO prices
        USING daily_prices AS staging
        ON prices.id = staging.id AND prices.date = PARSE_DATE('%F', "{str(datetime.today().date())}") AND prices.date > DATE_SUB(CURRENT_DATE(), INTERVAL 3 DAY)
        WHEN NOT MATCHED THEN
            INSERT (id, date, eur, usd)
            VALUES (staging.id, staging.date, staging.eur, staging.usd)
    """

    client.query(merge_job, job_config=config, project="mtg-rest")
    try:
        r2 = job.result()
    except:
        print(job.errors)