from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field

from server.models.survey import SDTProfile


class Job(BaseModel):
    job_id: int
    title: str
    description: str
    location: str
    company: EmailStr
    skills: List[str]


class CompanySchema(BaseModel):
    # - COMPANY ATTRIBUTES -
    iscompany: bool = Field(...)
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=12)

    # - JOB ATTRIBUTES -
    sdt_profile: Optional[SDTProfile]
    jobs: List[Job] = Field(default_factory=list)
    description: Optional[str] = Field(None)

    # - NOT NECESSARY YET -
    logo: Optional[str] = Field(None)

    # - MATCHING ATTRIBUTES -
    potential_applicants: Optional[List[str]] = Field(default_factory=list)
    has_matched: Optional[List] = Field(default_factory=list)

    class Config:
        schema_extra = {
            "example": {
                "iscompany": True,
                "name": "Company Name",
                "email": "jdoe@x.edu.ng",
                "password": "password123456",
                "sdt_profile": {
                    "autonomy_support": 3,
                    "competence_support": 4,
                    "relatedness_support": 2.5,
                    "growth_and_personal_alignment": 5,
                },
                "jobs": [
                    {
                        "job_id": "AUTOMATICALLY GENERATED, DO NOT PROVIDE",
                        "title": "Software Engineer",
                        "description": "We are looking for a software engineer to join our team.",
                        "location": "Lagos, NG",
                        "email": "EMAIL OF THIS COMPANY, DO NOT PROVIDE",
                        "skills": ["docker", "devops", "python", "ai"],
                    }
                ],
                "logo": "https://example.com/logo.png",
                "description": "We are looking for a software engineer to join our team.",
                "potential_applicants": ["John Doe", "Jane Doe"],
                "has_matched": ["Jonathan Doe"],
            }
        }


class UpdateCompanyModel(BaseModel):
    # - COMPANY ATTRIBUTES -
    iscompany: Optional[bool]
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

    # - JOB ATTRIBUTES -
    sdt_profile: Optional[SDTProfile]
    jobs: Optional[List[Job]]
    description: Optional[str]

    # - NOT NECESSARY YET -
    logo: Optional[str]

    # - MATCHING ATTRIBUTES -
    potential_applicants: Optional[List[str]]
    has_matched: Optional[List]

    class Config:
        schema_extra = {
            "example": {
                "iscompany": True,
                "name": "Company Name",
                "email": "jdoe@x.edu.ng",
                "password": "password123456",
                "sdt_profile": {
                    "autonomy_support": 3,
                    "competence_support": 4,
                    "relatedness_support": 2.5,
                    "growth_and_personal_alignment": 5,
                },
                "jobs": [
                    {
                        "job_id": "AUTOMATICALLY GENERATED, DO NOT PROVIDE",
                        "title": "Software Engineer",
                        "description": "We are looking for a software engineer to join our team.",
                        "location": "Lagos, NG",
                        "email": "EMAIL OF THE COMPANY, DO NOT PROVIDE",
                        "skills": ["full-stack", "javascript", "typescript", "openapi"],
                    }
                ],
                "logo": "https://example.com/logo.png",
                "description": "We are looking for a software engineer to join our team.",
                "potential_applicants": ["John Doe", "Jane Doe"],
                "has_matched": ["Jonathan Doe"],
            }
        }


def ResponseModel(data, message):
    return {
        "code": 200,
        "message": message,
        "data": [data],
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
