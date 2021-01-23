from typing import Optional

from pydantic import BaseModel


class Products(BaseModel):
    name: str
    value: float
    image: Optional[str]
