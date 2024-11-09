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
    applicant = await retrieve_applicant(email)
    companies = await retrieve_companies()
    if applicant:
        matched_companies = match_fitting_company(applicant, companies)
        return f"{applicant} | {matched_companies}"
    return ErrorResponseModel("An error occurred.", 404, "Applicant doesn't exist.")


@router.get("/company/{email}", response_description="Match company to many applicants")
async def match_company_to_applicant(email):
    company = await retrieve_company(email)
    applicants = await retrieve_applicants()
    if company:
        matched_applicants = match_fitting_applicant(company, applicants)
        return f"{company} | {matched_applicants}"
    return ErrorResponseModel("An error occurred.", 404, "Company doesn't exist.")
