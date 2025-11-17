from fastapi import FastAPI


app = FastAPI()

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.get("/")
# def root():
#     return {"message": "Hello World"}
#
# #path parameters
# @app.get("/users/{users_id}")
# def read_user(users_id: int):
#     return {"user_id": users_id, "name": "John Doe"}
#
# #query Parameters
# @app.get("/items/")
# def read_items(skip: int = 0, limit: int = 10):
#     return {"skip": skip, "limit": limit}
#

#GET Method
@app.get("/items/")
def read_item():
    return {"items": ["item1", "item2", "item3"]}

#POST Method
@app.post("/items/")
def create_item(name: str, price: float):
    return {"item_name": name, "item_price": price}
#PUT Method
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_name": name, "item_price": price, "item_id": item_id}
#DELETE Method
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"item {item_id} deleted"}