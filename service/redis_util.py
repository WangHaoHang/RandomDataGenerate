import redis
import json
from kazoo.client import KazooClient

host_url = '192.168.8.102'
host_port = 6379
zk = KazooClient(hosts=host_url)
class RedisUtil(object):
    def __init__(self):
        self.host = host_url
        self.port = host_port
if __name__ == '__main__':
    zk.start()
    value = zk.create('/testplatform/test',b'this is a test')
    zk.stop()
    print(value)
    # conn = redis.Redis(host_url,host_port)
    # conn.set('hang','123')
    # print(conn.get('hang').decode('utf-8'))