from fastapi import APIRouter, Body #type: ignore
from fastapi.encoders import jsonable_encoder #type: ignore

from server.matching_database import (
    find_match_for_applicant,
)
from server.models.matching import (
    ErrorResponseModel,
    ResponseModel,
    MatchingSchema,
)

router = APIRouter()