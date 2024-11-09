from pydantic import BaseModel
from typing_extensions import Annotated
from pydantic.functional_validators import AfterValidator


def validate_survey_field(v: float) -> float:
    if 0 > v or v > 5:
        raise ValueError("survey field should be within 0 to 5 inclusive")

    return v


class MentalProfile(BaseModel):
    work_life_balance: float
    growth_opportunities: float
    compensation: float
    supportive_leadership: float
    innovation: float


class Survey(BaseModel):
    # Autonomy support
    a1: Annotated[float, AfterValidator(validate_survey_field)]
    a2: Annotated[float, AfterValidator(validate_survey_field)]
    a3: Annotated[float, AfterValidator(validate_survey_field)]
    a4: Annotated[float, AfterValidator(validate_survey_field)]

    # Compentence Support
    b1: Annotated[float, AfterValidator(validate_survey_field)]
    b2: Annotated[float, AfterValidator(validate_survey_field)]
    b3: Annotated[float, AfterValidator(validate_survey_field)]
    b4: Annotated[float, AfterValidator(validate_survey_field)]

    # Relatedness Support
    c1: Annotated[float, AfterValidator(validate_survey_field)]
    c2: Annotated[float, AfterValidator(validate_survey_field)]
    c3: Annotated[float, AfterValidator(validate_survey_field)]
    c4: Annotated[float, AfterValidator(validate_survey_field)]

    # Growth and Personal Alignment
    d1: Annotated[float, AfterValidator(validate_survey_field)]
    d2: Annotated[float, AfterValidator(validate_survey_field)]
    d3: Annotated[float, AfterValidator(validate_survey_field)]
    d4: Annotated[float, AfterValidator(validate_survey_field)]

    def to_mental_profile(self) -> MentalProfile:
        return MentalProfile(
            work_life_balance=5,
            growth_opportunities=5,
            supportive_leadership=5,
            compensation=5,
            innovation=5,
        )
