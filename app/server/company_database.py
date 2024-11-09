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









# vvvvvvvvvv JUNK TESTING CODE vvvvvvvvvv 

async def populate():
    import json
    import os
    with open (os.path.join(os.getcwd(), "app/server/util/companies_sample.json"), "r") as file:
        companies = json.load(file)
        for company in companies:
            await add_company(company)

# NOT FIT FOR PRODUCTION. PASSWORD NOT HASHED!!! unicode-skull*7
async def add_company(company_data: dict):
    if await company_collection.find_one({"email": company_data["email"]}):
        return {}

    company = await company_collection.insert_one(company_data)
    new_company = await company_collection.find_one({"_id": company.inserted_id})
    return company_helper(new_company)

async def log_in_company(email: str, password: str):
    if await company_collection.find_one({"email": email, "password": password}):
        return True
    return False

async def retrieve_companies():
    companies = []
    async for company in company_collection.find():
        companies.append(company_helper(company))
    return companies


async def retrieve_company(email: str) -> Optional[dict]:
    company = await company_collection.find_one({"email": email})
    if company:
        return company_helper(company)


async def update_company(email: str, data: dict):
    if len(data) < 1:
        return False
    if await company_collection.find_one({"email": email}):
        return await company_collection.update_one({"email": email}, {"$set": data})


async def delete_company(email: str):
    if company := await company_collection.find_one({"email": email}):
        await company_collection.delete_one({"email": email})
    return company
