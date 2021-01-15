import pytest


@pytest.fixture
def base_path():
    api_name = "scores"
    env = "/dev"
    api_version = "v1"
    return f"/{api_name}{env}/{api_version}"
