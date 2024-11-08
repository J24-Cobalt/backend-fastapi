from typing import Dict, Optional, List, Any

from pydantic import BaseModel, EmailStr, Field # type: ignore

class Job(BaseModel):
    title: str
    description: str
    location: str

class CompanySchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=12)
    culture_metric: Dict[str, Any] = Field(default_factory=dict)
    jobs: List[Job] = Field(default_factory=list)
    logo: Optional[str] = Field(None)
    description: Optional[str] = Field(None)


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
            }
        }

class UpdateCompanyModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    culture_metric: Optional[Dict[str, Any]]
    jobs: Optional[List[Job]]
    logo: Optional[str]
    description: Optional[str]

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
