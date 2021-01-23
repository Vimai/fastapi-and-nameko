from enum import Enum

from fastapi import APIRouter

router = APIRouter()


class CarsBrands(str, Enum):
    toyota = "toyota"
    volkswagen = "volkswagen"
    honda = "honda"


@router.get("/cars/{car_brand}")
async def get_model(car_brand: CarsBrands):
    if car_brand == CarsBrands.toyota:
        return {"car_brand": car_brand, "message": "toyota!"}

    if car_brand.value == "volkswagen":
        return {"car_brand": car_brand, "message": "volkswagen"}

    return {"car_brand": car_brand, "message": "Have some residuals"}
