import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def cache_result(key, value):
    r.set(key, value)

def get_cache(key):
    return r.get(key)