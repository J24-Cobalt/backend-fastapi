from fastapi import APIRouter, Body #type: ignore
from fastapi.encoders import jsonable_encoder #type: ignore

from server.company_database import (
    add_company,
    delete_company,
    retrieve_company,
    retrieve_companies,
    update_company,
)
from server.models.company import (
    ErrorResponseModel,
    ResponseModel,
    CompanySchema,
    UpdateCompanyModel,
)

router = APIRouter()



@router.post("/", response_description="company data added into the database")
async def add_company_data(company: CompanySchema = Body(...)):
    company = jsonable_encoder(company)
    new_company = await add_company(company)
    return ResponseModel(new_company, "company added successfully.")

@router.get("/", response_description="companys retrieved")
async def get_companies():
    companys = await retrieve_companies()
    if companys:
        return ResponseModel(companys, "company data retrieved successfully")
    return ResponseModel(companys, "Empty list returned")


@router.get("/{id}", response_description="company data retrieved")
async def get_company_data(id):
    company = await retrieve_company(id)
    if company:
        return ResponseModel(company, "company data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "company doesn't exist.")

@router.put("/{id}")
async def update_company_data(id: str, req: UpdateCompanyModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_company = await update_company(id, req)
    if updated_company:
        return ResponseModel(
            "company with ID: {} name update is successful".format(id),
            "company name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the company data.",
    )

@router.delete("/{id}", response_description="company data deleted from the database")
async def delete_company_data(id: str):
    deleted_company = await delete_company(id)
    if deleted_company:
        return ResponseModel(
            "company with ID: {} removed".format(id), "company deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "companywith id {0} doesn't exist".format(id)
    )