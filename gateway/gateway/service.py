from fastapi import FastAPI
from gateway.api.router import router as api_router
from nameko.standalone.rpc import ClusterRpcProxy

CONFIG = {"AMQP_URI": "amqp://guest:guest@localhost:5672"}

PROJECT_NAME = 'projeto'
VERSION = '0.1.0'
DEBUG = True
API_PREFIX = ''


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/nameko")
async def nameko():
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.products.list()

    return result


