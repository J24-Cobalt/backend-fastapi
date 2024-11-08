from bson.objectid import ObjectId  # type: ignore
from typing import Optional
from server.database import company_collection


def company_helper(company) -> dict:
    return {
        "id": str(company["_id"]),
        "name": company["name"],
        "email": company["email"],
        "password": company["password"],
        "culture_metric": company["culture_metric"],
        "jobs": company["jobs"],
        "logo": company["logo"],
        "description": company["description"],
    }









# vvvvvvvvvv JUNK TESTING CODE vvvvvvvvvv 

# NOT FIT FOR PRODUCTION. PASSWORD NOT HASHED!!! unicode-skull*7
async def add_company(company_data: dict) -> dict:
    company = await company_collection.insert_one(company_data)
    new_company = await company_collection.find_one({"_id": company.inserted_id})
    return company_helper(new_company)


async def retrieve_companies():
    companies = []
    async for company in company_collection.find():
        companies.append(company_helper(company))
    return companies


async def retrieve_company(id: str) -> Optional[dict]:
    company = await company_collection.find_one({"_id": ObjectId(id)})
    if company:
        return company_helper(company)


async def update_company(id: str, data: dict):
    if len(data) < 1:
        return False
    if await company_collection.find_one({"_id": ObjectId(id)}):
        return await company_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )


async def delete_company(id: str):
    if company := await company_collection.find_one({"_id": ObjectId(id)}):
        await company_collection.delete_one({"_id": ObjectId(id)})
    return company
