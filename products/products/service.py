import logging

from nameko.rpc import rpc
from products import schemas

logger = logging.getLogger(__name__)


class ProductsService:

    name = "products"

    storage = []

    @rpc
    def get(self, product_id):
        product = self.storage[product_id]
        return product

    @rpc
    def list(self):
        return self.storage

    @rpc
    def create(self, product):
        product = schemas.Product(strict=True).load(product).data
        self.storage.append(product)
