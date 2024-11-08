from typing import Optional

from pydantic import BaseModel, EmailStr, Field # type: ignore


class ApplicantSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    years_of_employment: int = Field(...)
    employment_status: str = Field(...)
    university_gpa: float = Field(..., le=10.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "years_of_employment": 0,
                "employment_status": "employed",
                "univeristy_gpa": "10.0",
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    years_of_employment: Optional[str]
    employment_status: Optional[int]
    university_gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "years_of_employment": 0,
                "employment_status": "employed",
                "univeristy_gpa": "10.0",
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