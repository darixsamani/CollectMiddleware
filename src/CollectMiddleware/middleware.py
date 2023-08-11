from starlette import Request
from starlette.middleware.base import BaseHTTPMiddleware
from redis import Redis

class CollectMiddleware(BaseHTTPMiddleware):
    def __init__(self,app,redis_host: str, redis_port: str):
        
        super().__init__(app)
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis = Redis(self.redis_port, redis_host)

    async def dispatch(self, request: Request, call_next):
        # do something with the request object, for example
        # i want to collect data from Request object to redisTimeseris iwth this midddleware

        content_type = request.headers.get('Content-Type')
        print(f"content_type: {content_type}")
        
        # process the request and get the response    
        response = await call_next(request)
        
        return response