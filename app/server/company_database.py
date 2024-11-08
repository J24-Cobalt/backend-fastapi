from bson.objectid import ObjectId  # type: ignore
from typing import Optional
from server.database import company_collection


def company_helper(company) -> dict:
    return {
        "name": company["name"],
        "email": company["email"],
        "password": company["password"],
        "culture_metric": company["culture_metric"],
        "jobs": company["jobs"],
        "logo": company["logo"],
        "description": company["description"],
    }


# NOT FIT FOR PRODUCTION. PASSWORD NOT HASHED!!! unicode-skull*7
async def add_company(applicant_data: dict) -> dict:
    applicant = await company_collection.insert_one(applicant_data)
    new_applicant = await company_collection.find_one({"_id": applicant.inserted_id})
    return company_helper(new_applicant)


async def retrieve_companies():
    await company_collection.find().to_list()


async def retrieve_company(id: str) -> Optional[dict]:
    applicant = await company_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        return company_helper(applicant)


async def update_company(id: str, data: dict):
    if len(data) < 1:
        return False
    if await company_collection.find_one({"_id": ObjectId(id)}):
        return await company_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )


async def delete_company(id: str):
    if applicant := await company_collection.find_one({"_id": ObjectId(id)}):
        await company_collection.delete_one({"_id": ObjectId(id)})
    return applicant
