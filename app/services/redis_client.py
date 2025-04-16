import redis 
import os

redis_host = os.env("REDIS_HOST", "localhost")
redis_port = int(os.env("REDIS_PORT",123))

redis_client = redis.Redis(host = redis_host , port=redis_port ,decode_responses= True)