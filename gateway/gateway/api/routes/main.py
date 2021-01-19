from fastapi import APIRouter

from gateway.api.routes import products

router = APIRouter()
router.include_router(products.router, prefix="/products")
