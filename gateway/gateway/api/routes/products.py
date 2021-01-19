from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Products(BaseModel):
    name: str
    value: float


@router.post("")
async def create_product(product: Products):
    return product
