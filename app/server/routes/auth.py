from typing import Dict, Optional
from server.models.applicant import ApplicantSchema
from server.database import applicant_collection
from server.app import app
from random import randint
import sys

sessions: Dict[str, int] = {}


@app.post("/register")
async def register(info: ApplicantSchema):
    if not await applicant_collection.find_one({"username": info.username}):
        await applicant_collection.insert_one(info)


@app.get("/login")
async def login(username: str, password: str) -> Optional[int]:
    if await applicant_collection.find_one(
        {"username": username, "password": password}
    ):
        session_id = randint(0, sys.maxsize)
        sessions[username] = session_id
        return session_id
    else:
        return None


@app.get("/users/{username}")
async def get_user(username: str) -> Optional[ApplicantSchema]:
    return await applicant_collection.find_one({"username": username})
