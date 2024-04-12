


import pytest
from kafka import KafkaProducer,KafkaConsumer

@pytest.fixture(scope='module')
def kafka_setup():
     # Setup Kafka producer and consumer
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],group_id='test-group',auto_offset_reset='earliest')
    yield producer, consumer

    #Cleanup
    producer.close()
    consumer.close()


def test_odd_number_stream_processing(kafka_setup):
    producer, consumer = kafka_setup

    # Send a message
    producer.send('numbers', value='11'.encode('utf-8'))
    producer.flush()

    


   # Configure the consumer to read from the output topic
    consumer.subscribe(["odd-numbers"])
    try:
        for message in consumer:
            message_text = message.value.decode('utf-8')
            assert message_text == '11'
            break
    except Exception as e:
        pytest.fail(f"Failed to consume processed messages: {e}")



def test_even_number_stream_processing(kafka_setup):
    producer, consumer = kafka_setup

    # Send a message
    producer.send('numbers', value='22'.encode('utf-8'))
    producer.flush()

   # Configure the consumer to read from the output topic
    consumer.subscribe(["even-numbers"])
    try:
        for message in consumer:
            message_text = message.value.decode('utf-8')
            assert message_text == '22'
            break
    except Exception as e:
        pytest.fail(f"Failed to consume processed messages: {e}")
       