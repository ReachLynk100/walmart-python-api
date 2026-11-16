
from flask import Flask, jsonify

app = Flask(__name__)

# Sample Walmart product data
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 850.00,
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 550.00,
        "category": "Electronics"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 75.00,
        "category": "Accessories"
    }
]


@app.route("/")
def home():
    return jsonify({
        "application": "Walmart Product Management API",
        "status": "Running",
        "version": "1.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/products")
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>")
def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({
        "error": "Product not found"
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
