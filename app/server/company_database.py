from typing import Optional
from server.database import company_collection
from pydantic import EmailStr


def company_helper(company) -> dict:
    return {
        "iscompany": company["iscompany"],
        "name": company["name"],
        "email": company["email"],
        "password": company["password"],
        "sdt_profile": company["sdt_profile"],
        "jobs": company["jobs"],
        "logo": company["logo"],
        "description": company["description"],
    }


# vvvvvvvvvv JUNK TESTING CODE vvvvvvvvvv


async def populate():
    import json
    import os

    with open(
        os.path.join(os.getcwd(), "app/server/util/companies_sample.json"), "r"
    ) as file:
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


async def log_in_company(email: EmailStr, password: str):
    if await company_collection.find_one({"email": email, "password": password}):
        return True
    return False


async def retrieve_companies():
    companies = []
    async for company in company_collection.find():
        companies.append(company_helper(company))
    return companies


async def retrieve_company(email: EmailStr) -> Optional[dict]:
    company = await company_collection.find_one({"email": email})
    if company:
        return company_helper(company)


async def update_company(email: EmailStr, data: dict):
    if len(data) < 1:
        return False
    if await company_collection.find_one({"email": email}):
        return await company_collection.update_one({"email": email}, {"$set": data})


async def delete_company(email: EmailStr):
    if company := await company_collection.find_one({"email": email}):
        await company_collection.delete_one({"email": email})
    return company


async def delete_all_companies():
    await company_collection.delete_many({})
    return True


async def get_job(job_id: int):
    if company := await company_collection.find_one(
        {"jobs.job_id": job_id},
    ):
        return (job for job in company["jobs"] if job["job_id"] == job_id)
