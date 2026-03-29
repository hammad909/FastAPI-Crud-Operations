from fastapi import Depends, FastAPI
import db_models
from model import Product
from database import sessionLocal
from database import engine
from sqlalchemy.orm import Session

app = FastAPI()

#create db table for us
#it cant create db for us only table
db_models.Base.metadata.create_all(bind=engine)



def get_db():
   db = sessionLocal()
   try:
      yield db
   finally:
      db.close()




products = [
    Product(id=1, name="Laptop", description="Gaming laptop", price=1200.50, quantity=5),
    Product(id=2, name="Phone", description="Android smartphone", price=500.00, quantity=10),
    Product(id=3, name="Headphones", description="Noise cancelling", price=150.75, quantity=15),
    Product(id=4, name="Keyboard", description="Mechanical keyboard", price=80.99, quantity=20),
    Product(id=5, name="Mouse", description="Wireless mouse", price=40.25, quantity=25)
]

@app.get("/")
def get_main():
    return "Server Started. Welcome"


@app.get("/productslist")
def get_product_list(db : Session = Depends(get_db)):
    #query
    db_product = db.query(db_models.Product).all()
    return  db_product

@app.get("/product/{id}")
def get_productP_by_id(id : int,db : Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        return db_product
    return  "product not found"


@app.post("/product")
def add_product(product : Product, db : Session = Depends(get_db)):
    db.add(db_models.Product(**product.model_dump()))
    db.commit()


@app.put("/product/add")
def Put_product_data(id : int, product : Product, db : Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
         db_product.name = product.name
         db_product.description = product.description
         db_product.price = product.price
         db_product.quantity = product.quantity
         db.commit()
         return "successfully Updated"
    else:
        return  "No product found"


@app.delete("/product_deletion/{id}")
def delete_product_data(id: int, db : Session = Depends(get_db)):
  db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
  if db_product:
     db.delete(db_product)
     db.commit()
     return "product Deleted!"
  else:
   return "product not found"