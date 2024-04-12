from application import send_message, consume_process_messages
from kafka import KafkaConsumer, KafkaProducer


def test_send_message():
    # Call the function to test
    send_message("test-topic", "Hello, Kafka!")

    # Setup Kafka consumer to read the message back
    consumer = KafkaConsumer("test-topic",
                             group_id='test-group',
                             bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest')

    # Consume the message
    for message in consumer:
        assert message.value == b"Hello, Kafka!"
        break  # assuming one message for simplicity



def test_process_messages():
    # Produce a test message
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send("test-topic", b"Test Message")
    producer.flush()

    # Call the consumer processing function (should be adjusted to your application's logic)
    consume_process_messages("test-topic")

    # Here, you should verify that the consumer processed the message correctly
    # This could involve checking a database, a file, or any other side effect of the message processing


