#/bin/bash
export ELASTIC_APM_SERVER_URL=https://54c919547253466797f598eddcb97096.apm.us-central1.gcp.cloud.es.io
export ELASTIC_APM_SECRET_TOKEN=2uSbzDmNmwZZwk9C9x
export ELASTICSEARCH_URL=https://fecf8161fad9496d88475e38af6aea15.us-central1.gcp.cloud.es.io:9243

cd src
/home/joao/.local/bin/gunicorn --config gunicorn.conf --log-config logging.conf -b :5000 server:app