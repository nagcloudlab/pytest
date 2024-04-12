

from application import send_message,consume_process_messages
from kafka import KafkaProducer,KafkaConsumer

def test_send_message():
  
    send_message('greetings', 'Hello, Kafka!')

    # Setup Kafka consumer
    consumer = KafkaConsumer('greetings', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    # Poll for new messages
    for message in consumer:
        # Decode the message
        message_text = message.value.decode('utf-8')
        print(message_text)
        assert message_text == 'Hello, Kafka!'
        break

    # Close the consumer
    consumer.close()


def test_consume_process_messages():
    # Setup Kafka producer
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    # Send a message
    producer.send('greetings', value='Hello, Kafka!'.encode('utf-8'))
    producer.flush()

    # Consume and process the message
    consume_process_messages('greetings')

    # Here, you should verify that the consumer processed the message correctly
    # This could involve checking a database, a file, or any other side effect of the message processing


