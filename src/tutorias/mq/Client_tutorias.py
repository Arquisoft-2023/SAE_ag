from rabbMQ.Rpc_client import client as tutoriasRpcClient
from dotenv import load_dotenv
import threading
import asyncio
import queue
import json
import os

load_dotenv()

urlQueue = str(os.environ.get("URI_QUEUE"))
idQueue = str(os.environ.get("ID_QUEUE"))

response_queue = queue.Queue()

def send(item):
    try:
        tutorias_rpc = tutoriasRpcClient(urlQueue, idQueue)
        print(" [x] Requesting...")
        # ejecutar_en_hilo(item, response_queue)
        # response = response_queue.get_nowait()
        response = tutorias_rpc.call(json.dumps(item))
        print(" [.] Got!")
        response = json.loads(response) # convertir a diccionario

        if tutorias_rpc.connection.is_closed:
            print(" [x] Channel is closed...")
            tutorias_rpc.connect()
            print(" [x] Reconnecting...")
        return response
    except Exception as e:
        print(e)
        return (str({ "description": "Error send rpc_client", "status_code": 500, "status": 500, "error": str(e)}))
 
async def do_call(item, response_queue, tutorias_rpc):
    response = await tutorias_rpc.call_async(json.dumps(item))
    response_queue.put(response)

def ejecutar_en_hilo(item, response_queue, tutorias_rpc):
    hilo = threading.Thread(target=asyncio.run, args=(do_call(item, response_queue, tutorias_rpc),))
    # hilo.setDaemon(True)
    hilo.start()

async def go(item):
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(None, send, item)
    return response

