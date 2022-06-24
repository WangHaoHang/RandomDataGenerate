import logging
import time

from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic


class KafkaProperty(object):
    def __init__(self):
        self.address = 'localhost'
        self.port = 9092
        self.client_id = 1
        self.topic_name = 'test'
        self.partitions = 1
        self.replication_factor = 1
        self.group_id = 1
        self.offer_set_method = 'earliest'


def warpper(cls_object):
    '''
    单例装饰器
    :param cls_object:
    :return:
    '''

    def inner(*args, **kwargs):
        if not hasattr(cls_object, 'obj'):
            setattr(cls_object, 'obj', cls_object(args, kwargs))
        getattr(cls_object, 'obj')

    return inner


# @warpper
class KafkaUtils(object):
    '''
    Kafka工具类
    '''

    def __init__(self):
        pass

    def create_topic(self, property: KafkaProperty):
        '''
        创建 topic
        :param property:
        :return:
        '''
        flag = True
        try:
            admin_client = KafkaAdminClient(bootstrap_servers=property.address + ":" + str(property.port),
                                            client_id=property.client_id)
            topic_list = [NewTopic(name=property.topic_name, num_partitions=property.partitions,
                                   replication_factor=property.replication_factor)]
            flag = admin_client.create_topics(new_topics=topic_list, validate_only=False)
        except Exception as e:
            logging.warning("create_topic --- happens error:{%s}", e)
            flag = False
        return flag

    def get_producer(self, property: KafkaProperty):
        '''

        :param property:
        :return:
        '''
        try:
            producer = KafkaProducer(bootstrap_servers=[property.address + ":" + str(
                property.port)])  # 此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
        except Exception as e:
            logging.error("get_producer --- happens error:{%s}", e)
        return producer

    def get_consumer(self, property: KafkaProperty):
        '''

        :param property:
        :return:
        '''
        try:
            consumer = KafkaConsumer(bootstrap_servers=[property.address + ":" + str(property.port)],
                                     group_id=str(property.group_id),
                                     auto_offset_reset=property.offer_set_method)
            consumer.subscribe([property.topic_name])
        except Exception as e:
            logging.error("get_consumer --- happens error:{%s}", e)
        return consumer


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
        producer.send('test', msg.encode('utf-8'))
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
    kafka_utils = KafkaUtils()
    kafka_utils.get_consumer()
    # Producer()
    Consumer()
    # create()
