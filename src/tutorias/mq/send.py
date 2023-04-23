import json
from rabbMQ.Rpc_client import client as tutoriasRpcClient

url = '127.0.0.1'
urlQueue = str(url)
idQueue = str('tutorias_rpc_queue')

tutorias_rpc = tutoriasRpcClient(urlQueue, idQueue)

def send(item):
    print(" [x] Requesting...")
    response = tutorias_rpc.call(json.dumps(item))
    print(" [.] Got!")
    response = json.loads(response) # convertir a diccionario
    return response

