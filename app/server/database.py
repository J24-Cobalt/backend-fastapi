import motor.motor_asyncio  # type: ignore
from bson.objectid import ObjectId  # type: ignore
from typing import Optional
import os

client = motor.motor_asyncio.AsyncIOMotorClient(
    open(os.path.join(os.getcwd(), "env"), "r").read().strip()
)
db = client.db
applicant_collection = db.get_collection("applicants_collection")
company_collection = db.get_collection("companies_collection")


def applicant_helper(applicant) -> dict:
    return {
        "id": str(applicant["_id"]),
        "fullname": applicant["fullname"],
        "email": applicant["email"],
        "years_of_employment": applicant["years_of_employment"],
        "employment_status": applicant["employment_status"],
        "age": applicant["age"],
        "gender": applicant["gender"],
        "intro": applicant["intro"],
        "avatar": applicant["avatar"],
        "work_experience": applicant["work_experience"],
        "education": applicant["education"],
        "skills": applicant["skills"],
        "mental_profile": applicant["mental_profile"],
        "cv": applicant["cv"],
        "applications": applicant["applications"],
    }













# vvvvvvvvvv JUNK TESTING CODE vvvvvvvvvv 

async def retrieve_applicants():
    applicants = []
    async for applicant in applicant_collection.find():
        applicants.append(applicant_helper(applicant))
    return applicants


# NOT FIT FOR PRODUCTION. PASSWORD NOT HASHED!!! unicode-skull*7
async def add_applicant(applicant_data: dict) -> dict:
    if await applicant_collection.find_one({"email": applicant_data["email"]}):
        return {}

    applicant = await applicant_collection.insert_one(applicant_data)
    new_applicant = await applicant_collection.find_one({"_id": applicant.inserted_id})
    return applicant_helper(new_applicant)


async def retrieve_applicant(email: str) -> Optional[dict]:
    applicant = await applicant_collection.find_one({"email": email})
    if applicant:
        return applicant_helper(applicant)


async def update_applicant(email: str, data: dict):
    if len(data) < 1:
        return False
    applicant = await applicant_collection.find_one({"email": email})
    if applicant:
        updated_applicant = await applicant_collection.update_one(
            {"email": email}, {"$set": data}
        )
        if updated_applicant:
            return True
        return False


async def delete_applicant(email: str):
    applicant = await applicant_collection.find_one({"email": email})
    if applicant:
        await applicant_collection.delete_one({"email": email})
        return True
