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