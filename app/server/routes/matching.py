from fastapi import APIRouter, Body  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore
from server.database import retrieve_applicants, retrieve_applicant
from server.company_database import retrieve_companies, retrieve_company

from server.models.matching import (
    ErrorResponseModel,
    ResponseModel,
    MatchingSchema,
)

router = APIRouter()


@router.get("/{id}-to-many", response_description="Match applicant to many companies")
async def match_applicant_to_companies(id):
    applicant = await retrieve_applicant(id)
    companies = await retrieve_companies()
    if applicant:
        return f"Found: {applicant} and {companies}"
    return ErrorResponseModel("An error occurred.", 404, "Applicant doesn't exist.")

