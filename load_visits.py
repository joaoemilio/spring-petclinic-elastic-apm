import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk
es = Elasticsearch(
        cloud_id= "webinar-observability:c291dGhhbWVyaWNhLWVhc3QxLmdjcC5lbGFzdGljLWNsb3VkLmNvbSQ5YmI5MjliYmNjNjg0ODUwOTM3MzFhODNhNmJjNDE3MSRiYjNmMjQ4ZGJhY2E0NGU2ODFiZWI2ODcwNGFjNmQwZQ==",
        http_auth=("elastic", "EtvdZtekqi3pxTlgangyM7kg"),
    )

with open('visitas.json') as f:
  data = json.load(f)

es.indices.create(index="visitas-2021-01", body=json.loads(open('visitas-mappings.json').read()))

# Using for loop
for i in data:
    print(i)
    es.index(index="visitas-2021-01", body=i)
    print("doc criado")