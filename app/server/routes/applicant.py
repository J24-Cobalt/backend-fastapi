from fastapi import APIRouter, Body #type: ignore
from fastapi.encoders import jsonable_encoder #type: ignore

from server.database import (
    add_applicant,
    delete_applicant,
    retrieve_applicant,
    retrieve_applicants,
    update_applicant,
)
from server.models.applicant import (
    ErrorResponseModel,
    ResponseModel,
    ApplicantSchema,
    UpdateApplicantModel,
)

router = APIRouter()

@router.post("/", response_description="Applicant data added into the database")
async def add_applicant_data(applicant: ApplicantSchema = Body(...)):
    applicant = jsonable_encoder(applicant)
    new_applicant = await add_applicant(applicant)
    return ResponseModel(new_applicant, "Applicant added successfully.")