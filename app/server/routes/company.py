from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr
from typing import Any
from random import randint
import sys

from server.company_database import (
    company_collection,
    add_company,
    delete_company,
    get_job,
    retrieve_company,
    retrieve_companies,
    update_company,
    populate,
    log_in_company,
    delete_all_companies,
)
from server.models.company import (
    ErrorResponseModel,
    ResponseModel,
    CompanySchema,
    UpdateCompanyModel,
)

router = APIRouter()


@router.post("/login")
async def login_company(email: EmailStr = Body(...), password: str = Body(...)):
    if await log_in_company(email, password):
        return {"message": "logged in successfully"}
    return ErrorResponseModel("failed to log in", 403, "invalid credentials")


@router.post("/populate")
async def populate_companies():
    await populate()
    return {"message": "companies populated successfully"}


@router.get("/jobs")
async def get_all_jobs():
    if companies := await retrieve_companies():
        jobs = []
        for company in companies:
            jobs.extend(company["jobs"])
        return jobs
    print("no companies???")


@router.post("/", response_description="company data added into the database")
async def add_company_data(company: CompanySchema = Body(...)):
    if new_company := await add_company(jsonable_encoder(company)):
        return ResponseModel(new_company, "company added successfully.")
    else:
        return ErrorResponseModel(
            "failed to add company", 403, "company already exists"
        )


@router.get("/", response_description="companys retrieved")
async def get_companies():
    if companies := await retrieve_companies():
        return ResponseModel(companies, "company data retrieved successfully")
    return ResponseModel([], "Empty list returned")


@router.get("/{email}", response_description="company data retrieved")
async def get_company_data(email: EmailStr):
    company = await retrieve_company(email)
    if company:
        return ResponseModel(company, "company data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "company doesn't exist.")


@router.put("/{email}")
async def update_company_data(email: EmailStr, req: UpdateCompanyModel = Body(...)):
    data = req.__dict__

    if data["jobs"]:
        return ErrorResponseModel(
            "invalid request",
            403,
            "do not use this endpoint to modify jobs, use /company/{email}/{id} instead",
        )

    updated_company = await update_company(email, data)
    if updated_company:
        return ResponseModel(
            "company with email: {} name update is successful".format(email),
            "company name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the company data.",
    )


@router.post("/{email}/{id}")
async def post_job(email: EmailStr, job: dict[str, Any]):
    if await retrieve_company(email):
        job["job_id"] = randint(0, sys.maxsize)
        job["email"] = email
        await company_collection.update_one({"email": email}, {"$push": {"jobs": job}})
        return ResponseModel("job posted successfully", "job posted successfully")
    return ErrorResponseModel("failed to post job", 404, "company doesn't exist")


@router.delete("/{email}/{id}")
async def remove_job(email: EmailStr, job_id: int):
    if company := await retrieve_company(email):
        if (
            company_job
            for company_job in company["jobs"]
            if company_job["job_id"] == job_id
        ):
            await company_collection.update_one(
                {"email": email},
                {"$pull": {"jobs": {"job_id": job_id}}},
            )
            return ResponseModel("job removed successfully", "job removed successfully")
        return ErrorResponseModel("failed to remove job", 404, "job doesn't exist")

    return ErrorResponseModel("failed to remove job", 404, "company doesn't exist")


@router.delete(
    "/{email}", response_description="company data deleted from the database"
)
async def delete_company_data(email: EmailStr):
    deleted_company = await delete_company(email)
    if deleted_company:
        return ResponseModel(
            "company with email: {0} removed".format(email),
            "company deleted successfully",
        )
    return ErrorResponseModel(
        "An error occurred", 404, "companywith email {0} doesn't exist".format(email)
    )


@router.delete("/delete_all/", response_description="DELETE ALL COMPANIES")
async def delete_all_companies_data():
    if await delete_all_companies():
        return ResponseModel("All companies removed", "companies deleted successfully")
    return ErrorResponseModel("An error occurred", 404, "companies doesn't exist")


@router.get("/job/{id}")
async def get_job_by_id(id: int):
    return await get_job(id)
