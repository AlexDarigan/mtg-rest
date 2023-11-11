from google.cloud import pubsub_v1
from datetime import datetime
import json

def chunk_documents(documents, chunk_size = 500):      
    for i in range(0, len(documents), chunk_size):  
        yield documents[i:i + chunk_size]
        
def publish_measure_requests(start, end):
    publisher = pubsub_v1.PublisherClient()
    initial = int(datetime.fromisoformat("19900101").year)
    terminal = int(datetime.fromisoformat("20200101").year)
    futures = []
    for y in range(initial, terminal):
        begin = datetime.fromisoformat(str(y) + "0101")
        end = datetime.fromisoformat(str(y) + "1231")
        x = {"begin": begin.isoformat(), "end": end.isoformat()}
        future = publisher.publish("projects/mtg-rest/topics/fetch", json.dumps(x).encode("utf8"))
        futures.append(future)
    return futures

def publish(run_id, cards):
    publisher = pubsub_v1.PublisherClient()
    total = len(cards)
    futures = []
    count = 0
    for chunk in chunk_documents(cards, chunk_size=500):
        body = {
            "runId": run_id,
            "batch_count": len(chunk),
            "batch_total": total,
            "chunk": chunk,
            "count": count,
        }
        print(f'{datetime.now()}: Sending Chunk {count}')
        future = publisher.publish("projects/mtg-rest/topics/cards", json.dumps(body).encode("utf8"))
        print(f'{datetime.now()}: Sent Chunk {count}')
        count += 1
        futures.append(future)
    return futures