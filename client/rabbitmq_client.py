import logging
import time

import pika
from pika.exceptions import AMQPConnectionError, AMQPChannelError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DefaultRabbitMQClient:
    def __init__(self, queue_name, delivery_mode, host, port, username, password, max_retries, retry_delay):
        self.queue_name = queue_name
        self.delivery_mode = delivery_mode
        self.credentials = pika.PlainCredentials(username, password)
        self.parameters = pika.ConnectionParameters(host=host, port=port, credentials=self.credentials)
        self.max_retries = max_retries
        self.retry_delay = retry_delay

        self.connection = None
        self.channel = None
        self.declared_queues = {}

    def setup_connection(self):
        try:
            self.connection = pika.BlockingConnection(self.parameters)
            self.channel = self.connection.channel()
            logger.info("RabbitMQ setup completed successfully.")
        except AMQPConnectionError as e:
            logger.error(f"Failed to connect to RabbitMQ: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            logger.info("RabbitMQ connection closed.")

    # todo: review retry mechanism
    def produce_message(self, message, queue_name):
        retry_count = 0
        while retry_count <= self.max_retries:
            try:
                if not self.connection or self.connection.is_closed:
                    logger.info("Connection closed, attempting to reconnect...")
                    self.setup_connection()
                if queue_name not in self.declared_queues:
                    self.channel.queue_declare(queue=queue_name, durable=True)
                    self.declared_queues[queue_name] = True
                    logger.info("Queue declared successfully.")
                self.channel.basic_publish(
                    exchange='',
                    routing_key=queue_name,
                    body=message,
                    properties=pika.BasicProperties(
                        delivery_mode=self.delivery_mode,
                    )
                )
                logger.info("Message produced successfully.")
                return
            except (AMQPConnectionError, AMQPChannelError) as e:
                logger.error(f"Error producing message: {e}")
                retry_count += 1
                time.sleep(self.retry_delay)
                if retry_count > self.max_retries:
                    logger.error("Maximum retry limit reached, message could not be produced.")
                    break
