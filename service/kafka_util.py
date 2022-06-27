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
        获取生产者
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
        获取消费者
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


if __name__ == '__main__':
    kafka_utils = KafkaUtils()
    prop = KafkaProperty()
    consumer = kafka_utils.get_consumer(prop)
    consumer.subscribe(topics=['test'])
    while True:
        message = consumer.poll(3)
        for k,v in message.items():
            if k is None:
                continue
            else:
                print(k,v)
    # Producer()
    # Consumer()
    # create()
