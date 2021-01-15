from fastapi import FastAPI
from nameko.standalone.rpc import ClusterRpcProxy
from pydantic import BaseModel

CONFIG = {"AMQP_URI": "amqp://guest:guest@localhost:5672"}

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/nameko")
async def nameko():
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.products.list()

    return result


class Products(BaseModel):
    name: str
    value: float


@app.post("/products")
async def create_product(product: Products):
    return product
