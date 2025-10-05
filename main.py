from message_processor import MessageProcessor
from rabbit_mq_wrapper import RabbitMQWrapper

if __name__ == "__main__":
    rabbit_mq_wrapper = RabbitMQWrapper()
    message_processor = MessageProcessor()

    rabbit_mq_wrapper.consume_messages(message_processor.process_message)
