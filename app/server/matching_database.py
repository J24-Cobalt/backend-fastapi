from bson.objectid import ObjectId  # type: ignore
from server.database import company_collection, applicant_collection


async def find_match_for_applicant(id: str):
    applicant = await applicant_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        return "matching in progress"


async def find_match_for_company(id: str):
    company = await company_collection.find_one({"_id": ObjectId(id)})
    if company:
        return "matching in progress"

