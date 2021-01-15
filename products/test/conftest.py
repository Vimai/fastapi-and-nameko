import pytest
from nameko import config


@pytest.fixture
def test_config(rabbit_config):
    with config.patch({}):
        yield


@pytest.fixture
def product():
    return {
        "id": "LZ127",
        "title": "LZ 127",
        "passenger_capacity": 72,
        "maximum_speed": 130,
        "in_stock": 11,
    }


@pytest.fixture
def products(create_product):
    return [
        create_product(
            id="LZ127",
            title="LZ 127 Graf Zeppelin",
            passenger_capacity=20,
            maximum_speed=128,
            in_stock=10,
        ),
        create_product(
            id="LZ129",
            title="LZ 129 Hindenburg",
            passenger_capacity=50,
            maximum_speed=135,
            in_stock=11,
        ),
        create_product(
            id="LZ130",
            title="LZ 130 Graf Zeppelin II",
            passenger_capacity=72,
            maximum_speed=135,
            in_stock=12,
        ),
    ]
