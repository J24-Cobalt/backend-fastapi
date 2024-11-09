from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr

from server.database import (
    add_applicant,
    delete_applicant,
    retrieve_applicant,
    retrieve_applicants,
    update_applicant,
    populate,
    log_in_applicant,
    delete_all_applicants,
    submit_applicant_survey,
    applicant_collection,
)
from server.models.applicant import (
    ErrorResponseModel,
    ResponseModel,
    ApplicantSchema,
    UpdateApplicantModel,
)
from server.models.survey import Survey

router = APIRouter()


@router.post("/login")
async def login_applicant(email: EmailStr = Body(...), password: str = Body(...)):
    if await log_in_applicant(email, password):
        return {"message": "logged in successfully"}
    return ErrorResponseModel("failed to log in", 403, "invalid credentials")


@router.post("/populate")
async def populate_applicants():
    await populate()
    return {"message": "applicants populated successfully"}


@router.post("/", response_description="Applicant data added into the database")
async def add_applicant_data(applicant: ApplicantSchema = Body(...)):
    if new_applicant := await add_applicant(jsonable_encoder(applicant)):
        return ResponseModel(new_applicant, "Applicant added successfully.")
    else:
        return ErrorResponseModel(
            "failed to add applicant", 403, "applicant already exists"
        )


@router.get("/", response_description="Applicants retrieved")
async def get_applicants():
    applicants = await retrieve_applicants()
    if applicants:
        return ResponseModel(applicants, "Applicant data retrieved successfully")
    return ResponseModel(applicants, "Empty list returned")


@router.get("/{email}", response_description="Applicant data retrieved")
async def get_applicant_data(email: EmailStr):
    applicant = await retrieve_applicant(email)
    if applicant:
        return ResponseModel(applicant, "Applicant data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Applicant doesn't exist.")


@router.put("/{email}")
async def update_applicant_data(email: EmailStr, req: UpdateApplicantModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_applicant = await update_applicant(email, req)
    if updated_applicant:
        return ResponseModel(
            "Applicant with email: {} name update is successful".format(email),
            "Applicant name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the applicant data.",
    )


@router.delete(
    "/{email}", response_description="Applicant data deleted from the database"
)
async def delete_applicant_data(email: EmailStr):
    deleted_applicant = await delete_applicant(email)
    if deleted_applicant:
        return ResponseModel(
            "Applicant with email: {} removed".format(email),
            "Applicant deleted successfully",
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Applicantwith email {0} doesn't exist".format(email)
    )


@router.delete("/delete_all/", response_description="DELETE ALL APPLICANTS")
async def delete_all_applicants_data():
    deleted_applicants = await delete_all_applicants()
    if deleted_applicants:
        return ResponseModel(
            "All applicants removed", "applicants deleted successfully"
        )
    return ErrorResponseModel("An error occurred", 404, "applicants doesn't exist")


@router.post("/survey/{email}")
async def submit_survey(email: EmailStr, survey: Survey):
    if not await applicant_collection.find_one({"email": email}):
        return ErrorResponseModel(
            "failed to submit applicant survey", 404, "applicant not found"
        )

    if await submit_applicant_survey(email, survey):
        return ResponseModel(
            "submitted applicant survey", "applicant survey submitted successfully"
        )
    else:
        return ErrorResponseModel(
            "failed to submit applicant survey",
            500,
            "failed to submit applicant survey",
        )
