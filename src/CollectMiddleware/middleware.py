from starlette import Request
from starlette.middleware.base import BaseHTTPMiddleware
from pymongo import MongoClient
from datetime import datetime

class CollectMiddleware(BaseHTTPMiddleware):
    def __init__(self,app,mongodb_uri: str,):
        
        super().__init__(app)
        self.client = MongoClient(self.mongodb_uri)
        self.db = self.client["CollectMiddleware"]
        self.collection = self.db.CollectMiddleware

    async def dispatch(self, request: Request, call_next):
        # do something with the request object, for example
        # i want to collect data from Request object to redisTimeseris with this midddleware
        
        client_host = request.client.host
        request_path = request.url.path
        request_methode = request.method
        schema_request = request.url.scheme
        port = request.url.port
        content_type = request.headers.get('Content-Type')
        user_agent = request.headers.get("user-agent")
        host = request.headers.get("host")
        connection = request.headers.get("connection")
        referer = reqort = request.headers.get("referer")
        accept_encoding = request.headers.get("accept-encoding")
        origin = request.headers.get("origin")
        request_port = request.url.port
        query_parametre_request = request.query_params
        path_parametre_request = request.path_params
        cokies_request = request.cookies
        accept = request.headers.get("accept")
        content_type = request.headers.get('Content-Type')
        authentification = request.headers.get("authorization")
        content_length = request.headers.get("content-length")
        accept_language = request.headers.get("accept-language")
        boby = await request.body()
        time = datetime.now()

        data = {
            "time": time,
            "client_host": client_host,
            "request_methode": request_methode,
            "schema_request": schema_request,
            "port": port,
            "content_type": content_type,
            "user_agent": user_agent,
            "host": host,
            "connection": connection,
            "content_length": content_length,
            "referer": referer,
            "accept_encoding": accept_encoding,
            "origin": origin,
            "request_port": request_port,
            "query_parametre_request": query_parametre_request,
            "path_parametre_request": path_parametre_request,
            "cokies_request": cokies_request,
            "accept": accept,
            "content_type": content_type,
            "authentification": authentification,
            "accept_language": accept_language,
            "boby": boby
        }

        self.collection.insert_one(data)


        response = await call_next(request)

        
        return response
