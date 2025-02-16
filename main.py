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

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Fiz"}]

# Query parameters - Next two routes
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    # return {"message": "This is a list of items."}
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: int, sample_query_param: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if q:
        # return {"item_id": item_id, "q": q}
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum odor amet, consectetuer adipiscing elit."
            }
        )
    # return {"item_id": item_id}
    return item

@app.get("/users")
async def list_users():
    return {"message": "This is a list of users."}

@app.get("/users/current")
async def get_current_user():
    return {"message": "This is the current user."}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum odor amet, consectetuer adipiscing elit."
            }
        )
    return item

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