from fastapi import APIRouter

from gateway.schemas.products import Products

router = APIRouter()


@router.post("")
async def create_product(product: Products):
    return product
