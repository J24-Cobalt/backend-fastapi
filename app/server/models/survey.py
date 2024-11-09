from pydantic import BaseModel
from typing_extensions import Annotated
from pydantic.functional_validators import AfterValidator


def validate_survey_field(v: float) -> float:
    if 0 > v or v > 5:
        raise ValueError("survey field should be within 0 to 5 inclusive")

    return v


class SDTProfile(BaseModel):
    autonomy_support: float
    competence_support: float
    relatedness_support: float
    growth_and_personal_alignment: float


class Survey(BaseModel):
    # Autonomy support
    a1: Annotated[float, AfterValidator(validate_survey_field)]
    a2: Annotated[float, AfterValidator(validate_survey_field)]
    a3: Annotated[float, AfterValidator(validate_survey_field)]
    a4: Annotated[float, AfterValidator(validate_survey_field)]

    # Competence Support
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

    def to_sdtprofile(self) -> SDTProfile:
        return SDTProfile(
            autonomy_support=(self.a1 + self.a2 + self.a3 + self.a4) / 4,
            competence_support=(self.b1 + self.b2 + self.b3 + self.b4) / 4,
            relatedness_support=(self.c1 + self.c2 + self.c3 + self.c4) / 4,
            growth_and_personal_alignment=(self.d1 + self.d2 + self.d3 + self.d4) / 4,
        )
