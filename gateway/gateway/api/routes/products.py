from typing import Optional

from fastapi import APIRouter
from gateway.schemas.products import Products

router = APIRouter()


@router.post("")
async def create_product(product: Products):
    return product


@router.get("/{item_id}")
async def read_product(item_id: int):
    return {"item_id": item_id}


@router.put("/{item_id}")
async def recreate_product(item_id: int, item: Products, q: Optional[str] = None):
    return {"item_id": item_id}
