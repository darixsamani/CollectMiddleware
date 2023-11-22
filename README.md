# CollectMiddleware



# How to using it

```python

from fastapi import FastAPI

app = FastAPI

app.add_middleware(CollectMiddleware, mongodb_uri="mongodb://localhost:27017/")


@app.get("/")
async def main():
    return {"message": "Hello World"}

```
