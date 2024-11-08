from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson import ObjectId
import os

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["testdb"]
users_collection = db["users"]

class User(BaseModel):
    name: str
    email: str
    age: int

def user_to_dict(user):
    user["_id"] = str(user["_id"])
    return user

@app.post("/users", response_model=dict)
async def create_user(user: User):
    result = users_collection.insert_one(user.dict())
    new_user = users_collection.find_one({"_id": result.inserted_id})
    return user_to_dict(new_user)

@app.get("/users", response_model=List[dict])
async def get_users():
    users = list(users_collection.find())
    return [user_to_dict(user) for user in users]

@app.get("/users/{user_id}", response_model=dict)
async def get_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_to_dict(user)
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=dict)
async def update_user(user_id: str, updated_user: User):
    result = users_collection.update_one(
        {"_id": ObjectId(user_id)}, {"$set": updated_user.dict()}
    )
    if result.modified_count == 1:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        return user_to_dict(user)
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
