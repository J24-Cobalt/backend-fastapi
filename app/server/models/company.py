from typing import Dict, Optional, List, Any

from pydantic import BaseModel, EmailStr, Field  # type: ignore


class Job(BaseModel):
    title: str
    description: str
    location: str


class CompanySchema(BaseModel):
    # - COMPANY ATTRIBUTES -
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=12)

    # - JOB ATTRIBUTES -
    culture_metric: Dict[str, Any] = Field(default_factory=dict)
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
                "name": "Company Name",
                "email": "jdoe@x.edu.ng",
                "password": "password123456",
                "culture_metric": {
                    "culture": "Good",
                    "environment": "Good",
                    "safety": "Good",
                },
                "jobs": [
                    {
                        "title": "Software Engineer",
                        "description": "We are looking for a software engineer to join our team.",
                        "location": "Lagos, NG",
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
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

    # - JOB ATTRIBUTES -
    culture_metric: Optional[Dict[str, Any]]
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
                "name": "Company Name",
                "email": "jdoe@x.edu.ng",
                "password": "password123456",
                "culture_metric": {
                    "culture": "Good",
                    "environment": "Good",
                    "safety": "Good",
                },
                "jobs": [
                    {
                        "title": "Software Engineer",
                        "description": "We are looking for a software engineer to join our team.",
                        "location": "Lagos, NG",
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
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
