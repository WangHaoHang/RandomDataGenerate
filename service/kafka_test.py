import time

from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic


def create():
    admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
    topic_list = []
    topic_list.append(NewTopic(name="example_topic", num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)


def Producer():
    producer = KafkaProducer(
        bootstrap_servers=['127.0.0.1:9092'])  # 此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]

    for i in range(3):
        msg = "msg %d" % i
        producer.send('example_topic', msg.encode('utf-8'))
        # producer.close()


def Consumer():
    consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092'], group_id='1',
                             auto_offset_reset='earliest')
    consumer.subscribe(['example_topic'])

    while True:
        message = consumer.poll(timeout_ms=5)
        time.sleep(3)
        print(message)


if __name__ == '__main__':
    Producer()
    # Consumer()
    # create()
