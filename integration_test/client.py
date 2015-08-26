import sys
import redis

class Client():

    def __init__(self):
        self.conn = redis.StrictRedis("redis")

    def set(self, key, value):
        self.conn.set(key, value)

    def get(self, key):
        return self.conn.get(key)

if __name__ == '__main__':
    client = Client()
    client.get(sys.argv[1])
