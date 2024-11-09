from fastapi import APIRouter, Body  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore

from server.company_database import (
    add_company,
    delete_company,
    retrieve_company,
    retrieve_companies,
    update_company,
    populate,
    log_in_company,
)
from server.models.company import (
    ErrorResponseModel,
    ResponseModel,
    CompanySchema,
    UpdateCompanyModel,
)

router = APIRouter()

@router.post("/login")
async def login_company(email: str = Body(...), password: str = Body(...)):
    if await log_in_company(email, password):
        return {"message": "logged in successfully"}
    return ErrorResponseModel("failed to log in", 403, "invalid credentials")

@router.post("/populate")
async def populate_companies():
    await populate()
    return {"message": "companies populated successfully"}

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
    companys = await retrieve_companies()
    if companys:
        return ResponseModel(companys, "company data retrieved successfully")
    return ResponseModel(companys, "Empty list returned")


@router.get("/{email}", response_description="company data retrieved")
async def get_company_data(email):
    company = await retrieve_company(email)
    if company:
        return ResponseModel(company, "company data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "company doesn't exist.")


@router.put("/{email}")
async def update_company_data(email: str, req: UpdateCompanyModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_company = await update_company(email, req)
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


@router.delete(
    "/{email}", response_description="company data deleted from the database"
)
async def delete_company_data(email: str):
    deleted_company = await delete_company(email)
    if deleted_company:
        return ResponseModel(
            "company with email: {0} removed".format(email),
            "company deleted successfully",
        )
    return ErrorResponseModel(
        "An error occurred", 404, "companywith email {0} doesn't exist".format(email)
    )
