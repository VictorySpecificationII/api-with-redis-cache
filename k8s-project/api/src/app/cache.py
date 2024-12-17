# app/cache.py
import redis
import json
from datetime import timedelta
from fastapi import HTTPException
import memcache
import json

# Updated Redis connection to Kubernetes service (assuming `redis-master` is the service name)
redis_client = redis.Redis(
    host='redis-master.default.svc.cluster.local',  # Redis service in Kubernetes
    port=6379,  # Default Redis port
    db=0,  # Default Redis database
    decode_responses=True  # To handle string responses
)

def cache_response(key: str, data: dict, timeout_seconds: int = 60):
    """Store API response in Redis cache with a TTL (time-to-live)."""
    redis_client.setex(key, timedelta(seconds=timeout_seconds), json.dumps(data))

def get_from_cache(key: str):
    """Get cached response from Redis."""
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None

#-------------------------------------MEMCACHED IMPLEMENTATION-------------------------------------------#

# Initialize Memcached client
memcached_client = memcache.Client(["memcached.default.svc.cluster.local:11211"])

def cache_to_memcache(key: str, data: dict, timeout_seconds: int = 60):
    """Cache data in Memcached."""
    memcached_client.set(key, json.dumps(data), time=timeout_seconds)

def get_from_memcache(key: str):
    """Retrieve cached data from Memcached."""
    cached_data = memcached_client.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None
