import motor.motor_asyncio  # type: ignore
from bson.objectid import ObjectId  # type: ignore
from typing import Optional
import os

client = motor.motor_asyncio.AsyncIOMotorClient(open(os.path.join(os.getcwd(), 'env'), 'r').read().strip())

companies_db = client.companies
applicants_db = client.applicants
company_collection = companies_db.get_collection("companies_collection") 
applicant_collection = applicants_db.get_collection("applicants_collection") 


async def find_match_for_applicant(id: str):
    applicant = await applicant_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        return "matching in progress"
    
async def find_match_for_company(id: str):
    company = await company_collection.find_one({"_id": ObjectId(id)})
    if company:
        return "matching in progress"