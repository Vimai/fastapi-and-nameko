from fastapi import APIRouter

from gateway.schemas.products import Products

router = APIRouter()


@router.post("")
async def create_product(product: Products):
    return product


@router.get("/{item_id}")
async def read_product(item_id: int):
    return {"item_id": item_id}
