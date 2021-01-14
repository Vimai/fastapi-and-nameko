from marshmallow.exceptions import ValidationError
from nameko.testing.services import entrypoint_hook
from nameko.standalone.events import event_dispatcher
from nameko.testing.services import entrypoint_waiter
import pytest


from products.service import ProductsService


@pytest.fixture
def service_container(test_config, container_factory):
    container = container_factory(ProductsService)
    container.start()
    return container


def test_get_product(service_container):
    with entrypoint_hook(service_container, 'list') as list:
        loaded_product = list()

    assert [] == loaded_product
