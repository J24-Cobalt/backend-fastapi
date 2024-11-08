import motor.motor_asyncio #type: ignore
from bson.objectid import ObjectId #type: ignore

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.applicants

applicant_collection = database.get_collection("applicants_collection")


def applicant_helper(applicant) -> dict:
    return {
        "id": str(applicant["_id"]),
        "fullname": applicant["fullname"],
        "email": applicant["email"],
        "years_of_employment": applicant["years_of_employment"],
        "employment_status": applicant["employment_status"],
        "univeristy_gpa": applicant["university_gpa"],
    }


async def retrieve_applicants():
    applicants = []
    async for applicant in applicant_collection.find():
        applicants.append(applicant_helper(applicant))
    return applicants

async def add_applicant(applicant_data: dict) -> dict:
    applicant = await applicant_collection.insert_one(applicant_data)
    new_applicant = await applicant_collection.find_one({"_id": applicant.inserted_id})
    return applicant_helper(new_applicant)

async def retrieve_applicant(id: str) -> dict:
    applicant = await applicant_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        return applicant_helper(applicant)

async def update_applicant(id: str, data: dict):
    if len(data) < 1:
        return False
    applicant = await applicant_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        updated_applicant = await applicant_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_applicant:
            return True
        return False

async def delete_applicant(id: str):
    applicant = await applicant_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        await applicant_collection.delete_one({"_id": ObjectId(id)})
        return True