import logging

import redis
import json
from kazoo.client import KazooClient

# host_url = '192.168.8.102'
# host_port = 6379

host_url = '114.96.81.229'
host_port = 5903

zk = KazooClient(hosts=host_url)


def singleton(clsObject):
    '''
    单例模式--装饰器方法
    :param clsObject: 类
    @singleton
    class RedisUtil(object):
        ...
        ...
    :return:
    '''

    def inner(*args, **kwargs):
        if not hasattr(clsObject, "obj"):
            obj = clsObject(*args, **kwargs)
            setattr(clsObject, "obj", obj)
        return getattr(clsObject, "obj")

    return inner


@singleton
class RedisUtil:

    def __init__(self):
        self.host = host_url
        self.port = host_port
        self.redis = redis.Redis(host_url, host_port)

    # 字符串
    def set_str(self, key, value):
        '''
        设置键值字符串
        :param key: 键 key
        :param value: 值 字符串
        :return: true:成功，false:错误
        '''
        flag = True
        try:
            flag = self.redis.set(key, value)
        except Exception as e:
            flag = False
            logging.error("redisUtil ---- set_str happens error! key:{%s},value:{%s},error:{%s}", key, value, e)
        return flag

    def get_str(self, key):
        '''
        获取键所对应的字符串
        :param key:
        :return:
        '''
        result = ''
        try:
            result = self.redis.get(key).decode('utf-8')
        except Exception as e:
            logging.error("redisUtil ---- get_str happens error! key:{%s},error:{%s}", key, e)
        return result

    def set_byte(self, key, value):
        '''
        设置键值字节
        :param key:
        :param value:
        :return:
        '''
        flag = True
        try:
            flag = self.redis.set(key, value.encode('utf-8'))
        except Exception as e:
            flag = False
            logging.error("redisUtil ---- set_byte happens error! key:{%s},value:{%s},error:{%s}", key, value, e)
        return flag

    def get_byte(self, key):
        '''
        获取键所对应的字节
        :param key:
        :return:
        '''
        result = ''
        try:
            result = self.redis.get(key)
        except Exception as e:
            logging.error("redisUtil ---- get_str happens error! key:{%s},error:{%s}", key, e)
        return result

    # 列表
    def lpush(self, key, value):
        '''
        列表 入栈
        :param key:
        :param value:
        :return:
        '''
        pass

    def rpop(self, key):
        '''
        列表 出栈
        :param key:
        :return:
        '''
        pass

    def brpop(self, key):
        '''
        列表 阻塞出栈
        :param key:
        :return:
        '''
        pass

    def lindex(self, key, index):
        '''
        列表 查找
        :param key:
        :param index:
        :return:
        '''
        pass

    def lrange(self, key, start, end):
        '''
        列表 范围遍历
        :param key:
        :param start:
        :param end:
        :return:
        '''
        pass

    def lsize(self, key):
        '''
        列表 长度
        :param key:
        :return:
        '''
        pass

    # 集合
    def sadd(self, key, *value):
        '''
        集合 增加
        :param key:
        :param value:
        :return:
        '''
        pass

    def srem(self, key, *value):
        '''
        集合 删除
        :param key:
        :param value:
        :return:
        '''
        pass

    def sismem(self, key, value):
        '''
        集合 成员是否存在
        :param key:
        :param value:
        :return:
        '''
        pass

    def slen(self, key):
        '''
        集合 长度
        :param key:
        :return:
        '''
        pass

    def smembers(self, key):
        '''
        集合 查找
        :param key:
        :return:
        '''
        pass

    # 散列
    def hmset(self, key_name, **kwargs):
        '''
        散列表 增加
        :param key_name:
        :param kwargs:
        :return:
        '''
        pass

    def hmget(self, key_name, *key):
        '''
        散列表 查找
        :param key_name:
        :param key:
        :return:
        '''
        pass

    def hdel(self, key_name, *key):
        '''
        散列表 删除
        :param key_name:
        :param key:
        :return:
        '''
        pass

    def hlen(self, key_name):
        '''
        散列表 集合大小
        :param key_name:
        :return:
        '''
        pass

    # 有序集合

    def zadd(self, key_name, **kwargs):
        '''
        有序集合 增加
        :param key_name:
        :param kwargs:
        :return:
        '''
        pass

    def zmem(self, key_name):
        '''
        有序集合 查找
        :param key_name:
        :return:
        '''
        pass

    def zrem(self, key_name, *member):
        '''
        有序集合 删除
        :param key_name:
        :param member:
        :return:
        '''
        pass

    def zlen(self, key_name):
        '''
        有序集合 集合长度
        :param key_name:
        :return:
        '''
        pass

    def zmdf(self, key_name, **kwargs):
        '''
        有序集合 修改
        :param key_name:
        :param kwargs:
        :return:
        '''
        pass


if __name__ == '__main__':
    obj = RedisUtil()
    print(id(RedisUtil))
    # print(id(RedisUtil))
    print(id(singleton))
    obj.set_str('hang', 'wang')
    print(obj.get_str('hang'))
    obj1 = RedisUtil()
    print(id(obj1))
    print(obj1.get_byte('hang'))

    # print(id(getattr(RedisUtil,'set_str')))

# conn = redis.Redis(host_url,host_port)
# conn.set('hang','123')
# print(conn.get('hang').decode('utf-8'))
