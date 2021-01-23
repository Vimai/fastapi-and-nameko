from fastapi import APIRouter

from .routes import products, users, cars

router = APIRouter()
router.include_router(products.router, prefix="/products")
router.include_router(users.router, prefix="/users")
router.include_router(cars.router, prefix="/cars")
