import os

import pika
from dotenv import load_dotenv
from pika.exceptions import AMQPConnectionError
from retry import retry

load_dotenv()


class RabbitMQWrapper:
    def __init__(self):
        self.connection_url = os.getenv('CLOUDAMQP_URL')

        self.consume_queue = os.getenv('CONSUME_QUEUE')

        self.connection = None
        self.init_connection()

    def init_connection(self):
        params = pika.URLParameters(self.connection_url)

        self.connection = pika.BlockingConnection(params)

    @retry(AMQPConnectionError, delay=5, jitter=(1, 3))
    def consume_messages(self, cbk):
        if not self.connection:
            self.init_connection()

        channel = self.connection.channel()
        channel.basic_consume(self.consume_queue, cbk, auto_ack=True)
        channel.start_consuming()
