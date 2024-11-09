from fastapi import APIRouter
from server.database import retrieve_applicants, retrieve_applicant
from server.company_database import retrieve_companies, retrieve_company
from server.util.matchmaking import match_fitting_applicant, match_fitting_company
from server.models.matching import ErrorResponseModel

router = APIRouter()


@router.get(
    "/applicant/{email}", response_description="Match applicant to many companies"
)
async def match_applicant_to_companies(email):
    if (applicant := await retrieve_applicant(email)) and (
        companies := await retrieve_companies()
    ):
        return match_fitting_company(applicant, companies)
    return ErrorResponseModel("An error occurred.", 404, "Applicant doesn't exist.")


@router.get("/company/{email}", response_description="Match company to many applicants")
async def match_company_to_applicant(email):
    company = await retrieve_company(email)
    applicants = await retrieve_applicants()
    if (company := await retrieve_company(email)) and (
        applicants := await retrieve_applicants()
    ):
        return match_fitting_applicant(company, applicants)
    return ErrorResponseModel("An error occurred.", 404, "Company doesn't exist.")
