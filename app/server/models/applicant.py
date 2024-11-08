from typing import Dict, Optional, List, Any

from pydantic import BaseModel, EmailStr, Field # type: ignore

class WorkExperience(BaseModel):
    company: str
    position: str
    start_date: str  #YYYY-MM-DD
    end_date: Optional[str] = None  # YYYY-MM-DD or none if still employed
    description: Optional[str] = None


class Education(BaseModel):
    institution: str
    degree: str
    start_date: str  #YYYY-MM-DD
    end_date: Optional[str] = None  # YYYY-MM-DD or none if still employed
    score: Optional[float] = None  # if applicable


class ApplicantSchema(BaseModel):
    fullname: str = Field(...)
    username: str = Field(...)
    password: str = Field(..., min_length=12)
    email: EmailStr = Field(...)
    years_of_employment: Optional[int] = Field(0)
    employment_status: str = Field("unemployed")
    age: Optional[int] = Field(None, ge=0)
    gender: Optional[str] = Field(None, pattern=r'^(Male|Female|Other)$') 
    intro: Optional[str] = Field(None, max_length=250)  # Short description
    avatar: Optional[str] = Field(None)  # URL to avatar image
    work_experience: Optional[List[WorkExperience]] = Field(default_factory=list)
    education: Optional[List[Education]] = Field(default_factory=list)
    skills: Optional[List[str]] = Field(default_factory=list)  # List of skills
    mental_profile: Optional[Dict[str, Any]] = Field(default_factory=dict)  # Mental profile as a dict
    cv: Optional[str] = Field(None)  # URL or path to the CV
    applications: Optional[List[Dict[str, Any]]] = Field(default_factory=list)  # List of applications

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "username": "Janette Done",
                "password": "password123",
                "email": "jdoe@x.edu.ng",
                "years_of_employment": 5,
                "employment_status": "employed",
                "age": 30,
                "gender": "Male",
                "intro": "Experienced software developer with a passion for technology.",
                "avatar": "https://example.com/avatar.jpg",
                "work_experience": [
                    {
                        "company": "TechCorp",
                        "position": "Senior Developer",
                        "start_date": "2018-06-01",
                        "end_date": "2023-08-01",
                        "description": "Developed scalable applications for clients."
                    }
                ],
                "education": [
                    {
                        "institution": "University of Example",
                        "degree": "Bachelor of Science in Computer Science",
                        "start_date": "2014-09-01",
                        "end_date": "2018-06-01",
                        "score": 3.8
                    }
                ],
                "skills": ["Python", "Django", "Machine Learning"],
                "mental_profile": {
                    "personality": "INTJ",
                    "strengths": ["Analytical", "Strategic"],
                    "weaknesses": ["Perfectionist"]
                },
                "cv": "https://example.com/cv.pdf",
                "applications": [
                    {"job_id": 1, "status": "pending", "date_applied": "2023-10-15"}
                ]
            }
        }


class UpdateApplicantModel(BaseModel):
    fullname: Optional[str]
    username: str = Field(...)
    password: str = Field(..., min_length=12)
    email: Optional[EmailStr]
    years_of_employment: Optional[int]
    employment_status: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    intro: Optional[str]
    avatar: Optional[str]
    work_experience: Optional[List[WorkExperience]]
    education: Optional[List[Education]]
    skills: Optional[List[str]]
    mental_profile: Optional[Dict[str, Any]]
    cv: Optional[str]
    applications: Optional[List[Dict[str, Any]]]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "username": "Janette Done",
                "password": "password123",
                "email": "jdoe@x.edu.ng",
                "years_of_employment": 5,
                "employment_status": "employed",
                "age": 30,
                "gender": "Male",
                "intro": "Experienced software developer with a passion for technology.",
                "avatar": "https://example.com/avatar.jpg",
                "work_experience": [
                    {
                        "company": "TechCorp",
                        "position": "Senior Developer",
                        "start_date": "2018-06-01",
                        "end_date": "2023-08-01",
                        "description": "Developed scalable applications for clients."
                    }
                ],
                "education": [
                    {
                        "institution": "University of Example",
                        "degree": "Bachelor of Science in Computer Science",
                        "start_date": "2014-09-01",
                        "end_date": "2018-06-01",
                        "score": 3.8
                    }
                ],
                "skills": ["Python", "Django", "Machine Learning"],
                "mental_profile": {
                    "personality": "INTJ",
                    "strengths": ["Analytical", "Strategic"],
                    "weaknesses": ["Perfectionist"]
                },
                "cv": "https://example.com/cv.pdf",
                "applications": [
                    {"job_id": 1, "status": "pending", "date_applied": "2023-10-15"}
                ]
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