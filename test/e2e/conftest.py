import pytest
from nameko import config
from nameko.testing.utils import find_free_port

from products.service import ProductsService

pytest_plugins = [
    "test.e2e.fixtures.envs",
]


@pytest.fixture
def test_config(rabbit_config):
    with config.patch({}):
        yield


@pytest.fixture
def products_service(container_factory, test_config):
    with config.patch(
        {
            "WEB_SERVER_ADDRESS": f"0.0.0.0:{find_free_port()}",
            "DB_URIS": {
                "scores_scores_dev:Base": "postgresql://postgres:password@localhost:5432/cred_corp_local"
            },
        }
    ):
        container = container_factory(ProductsService)
        container.start()
    return container
