import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def get(key):
    return r.get(key)

def set(key, value, ex=None):
    r.set(key, value, ex=ex)

def delete(key):
    r.delete(key)

def invalidate(pattern):
    for key in r.scan_iter(pattern):
        r.delete(key)