import redis
import json
from kazoo.client import KazooClient

# host_url = '192.168.8.102'
# host_port = 6379

host_url = '114.96.81.229'
host_port = 5903

zk = KazooClient(hosts=host_url)


class RedisUtil(object):
    def __init__(self):
        self.host = host_url
        self.port = host_port
        self.redis = redis.Redis(host_url, host_port)

    # 字符串
    def set_str(self, key, value):
        '''
        设置键值字符串
        :param key:
        :param value:
        :return:
        '''
        pass

    def get_str(self, key):
        '''
        获取键所对应的字符串
        :param key:
        :return:
        '''
        pass

    def set_byte(self, key, value):
        '''
        设置键值字节
        :param key:
        :param value:
        :return:
        '''
        pass

    def get_byte(self, key):
        '''
        获取键所对应的字节
        :param key:
        :return:
        '''
        pass

    # 列表
    def lpush(self, key, value):
        pass

    def rpop(self, key):
        pass

    def brpop(self, key):
        pass

    def lindex(self, key, index):
        pass

    def lrange(self, key, start, end):
        pass

    def lsize(self, key):
        pass

    # 集合
    def sadd(self, key, *value):
        pass

    def srem(self, key, *value):
        pass

    def sismem(self, key, value):
        pass

    def slen(self, key):
        pass

    def smembers(self, key):
        pass

    # 散列
    def hmset(self, key_name, **kwargs):
        pass

    def hmget(self, key_name, *key):
        pass

    def hdel(self, key_name, *key):
        pass

    def hlen(self, key_name):
        pass

    # 有序集合

    def zadd(self, key_name, **kwargs):
        pass

    def zrem(self, key_name, *member):
        pass

    def zlen(self, key_name):
        pass

    def zmdf(self, key_name, **kwargs):
        pass


if __name__ == '__main__':
    pass
# conn = redis.Redis(host_url,host_port)
# conn.set('hang','123')
# print(conn.get('hang').decode('utf-8'))
