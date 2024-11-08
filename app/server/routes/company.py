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



@router.post("/", response_description="Applicant data added into the database")
async def add_company_data(applicant: CompanySchema = Body(...)):
    applicant = jsonable_encoder(applicant)
    new_applicant = await add_company(applicant)
    return ResponseModel(new_applicant, "Applicant added successfully.")

@router.get("/", response_description="Applicants retrieved")
async def get_companies():
    applicants = await retrieve_companies()
    if applicants:
        return ResponseModel(applicants, "Applicant data retrieved successfully")
    return ResponseModel(applicants, "Empty list returned")


@router.get("/{id}", response_description="Applicant data retrieved")
async def get_company_data(id):
    applicant = await retrieve_company(id)
    if applicant:
        return ResponseModel(applicant, "Applicant data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Applicant doesn't exist.")

@router.put("/{id}")
async def update_company_data(id: str, req: UpdateCompanyModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_applicant = await update_company(id, req)
    if updated_applicant:
        return ResponseModel(
            "Applicant with ID: {} name update is successful".format(id),
            "Applicant name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the applicant data.",
    )

@router.delete("/{id}", response_description="Applicant data deleted from the database")
async def delete_company_data(id: str):
    deleted_applicant = await delete_company(id)
    if deleted_applicant:
        return ResponseModel(
            "Applicant with ID: {} removed".format(id), "Applicant deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Applicantwith id {0} doesn't exist".format(id)
    )