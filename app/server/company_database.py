import motor.motor_asyncio  # type: ignore
from bson.objectid import ObjectId  # type: ignore
from typing import Optional
import os

client = motor.motor_asyncio.AsyncIOMotorClient(open(os.path.join(os.getcwd(), 'env'), 'r').read().strip())

companies_db = client.companies
company_collection = companies_db.get_collection("companies_collection") 


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
    companies = []
    async for company in company_collection.find():
        companies.append(company_helper(company))
    return companies

async def retrieve_company(id: str) -> Optional[dict]:
    applicant = await company_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        return company_helper(applicant)


async def update_company(id: str, data: dict):
    if len(data) < 1:
        return False
    applicant = await company_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        updated_applicant = await company_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_applicant:
            return True
        return False


async def delete_company(id: str):
    applicant = await company_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        await company_collection.delete_one({"_id": ObjectId(id)})
        return True

