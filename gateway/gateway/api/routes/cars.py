from enum import Enum
from typing import Optional

from fastapi import APIRouter

router = APIRouter()


class CarsBrands(str, Enum):
    toyota = "toyota"
    volkswagen = "volkswagen"
    honda = "honda"


@router.get("/{car_brand}")
async def get_model(car_brand: CarsBrands):
    if car_brand == CarsBrands.toyota:
        return {"car_brand": car_brand, "message": "toyota!"}

    if car_brand.value == "volkswagen":
        return {"car_brand": car_brand, "message": "volkswagen"}

    return {"car_brand": car_brand, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/")
async def read_cars(skip: int = 0, limit: int = 10, color: Optional[str] = None):
    return fake_items_db[skip: skip + limit]
