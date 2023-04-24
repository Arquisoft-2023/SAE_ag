from rabbMQ.Rpc_client import client as tutoriasRpcClient
from dotenv import load_dotenv
import pika
import json
import os

load_dotenv()

urlQueue = str(os.environ.get("URI_QUEUE"))
idQueue = str(os.environ.get("ID_QUEUE"))

tutorias_rpc = tutoriasRpcClient(urlQueue, idQueue)

async def send(item):
    try:
        print(" [x] Requesting...")
        response = await tutorias_rpc.call_async(json.dumps(item))
        print(" [.] Got!")
        response = json.loads(response) # convertir a diccionario
        return response
    except Exception as e:
        print(e)
        return (str({ "description": "Error send rpc_client", "status_code": 500, "error": str(e)}))
 

