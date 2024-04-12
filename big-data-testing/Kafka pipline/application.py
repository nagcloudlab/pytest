

from kafka import KafkaProducer,KafkaConsumer

def send_message(topic, message):
    # Setup Kafka producer (assuming localhost:9092)
    producer = KafkaProducer(bootstrap_servers='localhost:9092')  # to get cluster metadata
    # Convert the message to bytes
    message_bytes = message.encode('utf-8')

    # Send the message
    producer.send(topic, partition=1, value=message_bytes)

    # Block until a single message is sent (or timeout)
    producer.flush()
def consume_process_messages(topic):
    """
    Consumes messages from a Kafka topic and processes them.
    """
    # Setup Kafka consumer
    consumer = KafkaConsumer(topic,
                             group_id='test-group',
                             bootstrap_servers="localhost:9092",
                             auto_offset_reset='earliest')

    # Process messages
    for message in consumer:
        print(f"Processing message: {message.value}")
        # Here you would process the message, e.g., save to a database, write to a file, etc.
        break  # assuming one message for simplicity

    # Close the consumer
    consumer.close()