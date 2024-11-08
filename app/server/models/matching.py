from typing import Dict, Optional, List, Any

from pydantic import BaseModel, EmailStr, Field  # type: ignore


class Job(BaseModel):
    title: str
    description: str
    location: str


class MatchingSchema(BaseModel):
    name: str = Field(...)
    company: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Company Name",
                "company": "Company Name",
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
