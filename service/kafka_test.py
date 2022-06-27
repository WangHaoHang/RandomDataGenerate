from service.kafka_util import KafkaUtils, KafkaProperty
import time
from threading import Thread


def send(topic_name, key_name):
    kafkautils = KafkaUtils()
    pro = KafkaProperty()
    producer = kafkautils.get_producer(property=pro)
    for i in range(1000):
        producer.send(topic=topic_name, value=str(i).encode('utf-8'), key=(key_name + str(i)).encode('utf-8'))
        time.sleep(1)


if __name__ == '__main__':
    a_thread = Thread(target=send, args=['test', 'a'])
    b_thread = Thread(target=send, args=['test', 'b'])
    a_thread.start()
    b_thread.start()
    while True:
        pass
    # Consumer()
    # create()
