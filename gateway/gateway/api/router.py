from fastapi import APIRouter

from .routes import products

router = APIRouter()
router.include_router(products.router, prefix="/products")
