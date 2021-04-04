from elasticsearch import Elasticsearch
import logging

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Able to Reach Elasticsearch!')
    else:
        print('Unable to Reach Elasticsearch!')
    return _es
    
if __name__ == '__main__':
  logging.basicConfig(level=logging.ERROR)
  connect_elasticsearch()