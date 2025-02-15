from enum import Enum
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/")
async def post():
    return {"message": "This is a POST request."}

@app.put("/")
async def put():
    return {"message": "This is a PUT request."}


@app.get("/items")
async def list_items():
    return {"message": "This is a list of items."}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users")
async def list_users():
    return {"message": "This is a list of users."}

@app.get("/users/current")
async def get_current_user():
    return {"message": "This is the current user."}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "Fruits"
    vegetables = "Vegatables"
    dairy = "Dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food name": food_name, "message": "You are healthy!"}
    elif food_name.value == "Fruits":
        return {"food name": food_name, "message": "You are still healthy, but like sweet things."}
    else:
        return {"food name": food_name, "message": "Most dairy items are savory, but some can be sweet."}