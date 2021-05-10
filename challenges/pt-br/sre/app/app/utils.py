import redis
from prettyconf import config

REDIS_HOST = config("REDIS_HOST")

redis_client = redis.Redis(host=REDIS_HOST)


def fetch_count_from_redis():
    counter = redis_client.get("counter") or 0
    return int(counter)


def store_count_in_redis(count):
    return redis_client.set("counter", count)
