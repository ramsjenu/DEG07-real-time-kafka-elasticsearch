from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(hosts=["http://localhost:9200"])

# Check if the index exists
if es.indices.exists(index='enriched_data'):
    print("Index exists")

    # Retrieve document count
    count = es.count(index='enriched_data')
    print(f"Document count: {count['count']}")

    # Retrieve some documents
    response = es.search(index='enriched_data', size=10)
    for hit in response['hits']['hits']:
        print(hit['_source'])
else:
    print("Index does not exist")
