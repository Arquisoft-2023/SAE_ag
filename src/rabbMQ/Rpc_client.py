import asyncio
import pika
import uuid


class client(object):

    def __init__(self, urlQueue, idQueue, username, password):
        self.urlQueue = urlQueue
        self.idQueue = idQueue
        self.username = username
        self.password = password
        self.credentials = pika.PlainCredentials(self.username, self.password)
        self.connect()
    
    def connect(self):
        self.connection = pika.BlockingConnection(
          pika.ConnectionParameters(host=self.urlQueue, credentials=self.credentials, heartbeat=360, blocked_connection_timeout=65))
        self.channel = self.connection.channel()
        # result = self.channel.queue_declare(queue='', exclusive=True)
        # result = self.channel.queue_declare(queue=self.idQueue)

        # Verificar si la cola existe
        queue_exists = self.check_queue_exists(self.idQueue)

        if not queue_exists:
            # Si la cola no existe, declararla con los atributos deseados
             result = self.channel.queue_declare(queue=self.idQueue, durable=True)
        else:
            result = self.channel.queue_declare(queue=self.idQueue, passive=True)
            # Si la cola existe, no es necesario declararla nuevamente
            pass

        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def check_queue_exists(self, queue_name):
        # Verificar si la cola existe
        result = self.channel.queue_declare(queue=queue_name, passive=True)
        return result.method.message_count >= 0

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, item):
        try: 
            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(
                exchange='',
                routing_key=self.idQueue,
                properties=pika.BasicProperties(
                    reply_to=self.callback_queue,
                    correlation_id=self.corr_id,
                ),
                body=item)
            self.connection.process_data_events(time_limit=None)
            self.response = self.response.decode('utf-8')
            return self.response
        except pika.exceptions.AMQPConnectionError:
            return "Channel is closed"

    async def call_async(self, item):
        loop = asyncio.get_running_loop()
        response = await loop.run_in_executor(None, self.call, item)
        return response
        
    