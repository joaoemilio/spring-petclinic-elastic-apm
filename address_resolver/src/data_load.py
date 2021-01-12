import csv
import json, os, sys, argparse, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file', required=True)
parser.add_argument('--index', dest='index', required=False, default='address')
parser.add_argument('--use_ssl', dest='use_ssl', action='store_true', default=False)
parser.add_argument('--es_host', dest='es_host', required=False)
parser.add_argument('--es_user', dest='es_user', required=False, default='elastic')
parser.add_argument('--es_password', dest='es_password', required=False, default='changeme')
parser.add_argument('--thread_count', dest='thread_count', required=False, default=8, type=int)
parser.add_argument('--chunk_size', dest='chunk_size', required=False, default=1000, type=int)
parser.add_argument('--timeout', dest='timeout', required=False, default=120,type=int)
parser.add_argument('--pipeline', dest='pipeline', required=False)


def handle_data_file(file_path, index):
    with open(file_path, 'r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            doc = dict(row)
            doc['_index'] = index
            doc['_type'] = "_doc"
            doc = {k: v for k, v in doc.items() if v is not None and v != ""}
            yield doc

if __name__ == '__main__':
    args = parser.parse_args()
    es = Elasticsearch(
        cloud_id="falabella-observability:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJGZlY2Y4MTYxZmFkOTQ5NmQ4ODQ3NWUzOGFmNmFlYTE1JDM5ZGE4OTNhZDQ2MDQ0MjU4ZTI4ZjFjZDJhZTg0NTU5",
        http_auth=("elastic", "KD9wTa71rUWxSTwagtBsKsLe"),
    )
    #es = Elasticsearch(hosts=[args.es_host], http_auth=(args.es_user, args.es_password), use_ssl=args.use_ssl, verify_certs=True, timeout=args.timeout)
    start = time.time()
    print(args.index);
    if (not es.indices.exists(index=args.index)):
        es.indices.create(index=args.index, body = json.loads(open('mapping.json').read()))
    cnt = 0
    indices=set()
    doc = handle_data_file(args.file, args.index)
    print(doc)
    for success, info in parallel_bulk(
            es,
            doc,
            thread_count=args.thread_count,
            chunk_size=args.chunk_size,
            timeout='%ss' % args.timeout,
            pipeline=args.pipeline
    ):
        if success:
            cnt += 1
            if cnt % args.chunk_size == 0:
                print('Indexed %s documents' % str(cnt), flush=True)
                sys.stdout.flush()
        else:
            print('Doc failed', info)
    print('DONE\nIndexed %s documents in %.2f seconds' % (
        cnt, time.time() - start
    ), flush=True)
    print('INDEXING COMPLETE',flush=True)
    es.indices.refresh(index=args.index)
    print('DATA LOAD COMPLETE',flush=True)
