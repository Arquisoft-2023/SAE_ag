import pika
import uuid

class client(object):

    def __init__(self, urlQueue, idQueue):
        self.urlQueue = urlQueue
        self.idQueue = idQueue
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.urlQueue))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, item):
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