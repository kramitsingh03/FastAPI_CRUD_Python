from fastapi import FastAPI
from models import Product
from database import session, engine
import database_models
app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Hello World "}

Products = [
    Product(id=1, name="Phone", description="budget Phone", price=99, quantity=10),
    Product(id=2, name="Gaming", description="budget Laptop", price=999, quantity=4),
    Product(id=3, name="Phone", description="budget Phone", price=99, quantity=10),
    Product(id=4, name="Gaming", description="budget Laptop", price=999, quantity=4),
    Product(id=5, name="Phone", description="budget Phone", price=99, quantity=10),
    Product(id=6, name="Gaming", description="budget Laptop", price=999, quantity=4)
]

@app.get("/products")
def get_all_products():
    # db = session()
    return Products  

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in Products:
        if product.id == id:
            return product

    return "Product not found!"

@app.post("/product")
def add_product(product: Product):
    Products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(Products)):
        if Products[i].id == id:
            Products[i] = product
            return "Product added successfully"

    return "No Product found"

@app.delete("/product/{id}")
def delete_product(id:int):
    for i in range(len(Products)):
        if Products[i].id == id:
            del Products[i]
            return "Delete Product successfully"
    return "Product not found"




#pip install sqlalchemy psycopg2