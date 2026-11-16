
from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "Running"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_get_products():
    client = app.test_client()
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_single_product():
    client = app.test_client()
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json["name"] == "Laptop"


def test_product_not_found():
    client = app.test_client()
    response = client.get("/products/999")

    assert response.status_code == 404
