from google.cloud import bigquery

def update_all(cards):
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