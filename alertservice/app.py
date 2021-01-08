# vi app.py  
from flask import Flask  
from flask import Flask
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)  

app.config['ELASTIC_APM'] = {
          'SERVICE_NAME': 'petclinic-python',
          'SECRET_TOKEN': 'fUdDairnKQ5L6CUq8U',         
          'SERVER_URL': 'https://e502ba7b9aac4941a32d366eb20628c0.apm.southamerica-east1.gcp.elastic-cloud.com:443'
}

apm = ElasticAPM(app)

@app.route('/')  
def index():   
 return "Hello World!"  
if __name__ == '__main__':   
 app.run(host='localhost', port=5000)