from fastapi.testclient import TestClient
from gateway.service import app


class TestProduct(object):

    def test_read_main(self):
        client = TestClient(app)

        response = client.get("/")
        assert 1 != 0
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}


    def test_read_main_2(self, products_service):
        client = TestClient(app)

        response = client.get("/nameko")

        assert response.status_code == 200
        assert response.json() == []

