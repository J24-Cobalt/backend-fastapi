from typing import Any, List


def mix_sdt(applicant_sdt: dict[str, Any], company_sdt: dict[str, Any]) -> float:
    return (
        applicant_sdt["autonomy_support"] * company_sdt["autonomy_support"]
        + applicant_sdt["competence_support"] * company_sdt["competence_support"]
        + applicant_sdt["relatedness_support"] * company_sdt["relatedness_support"]
        + applicant_sdt["growth_and_personal_alignment"]
        * company_sdt["growth_and_personal_alignment"]
    )


def match_fitting_company(
    applicant: dict[str, Any], companies: List[dict[str, Any]], take: int = 5
):
    applicant_sdt = applicant["sdt_profile"]
    return sorted(
        companies,
        key=lambda company: mix_sdt(applicant_sdt, company["sdt_profile"]),
        reverse=True,
    )[:take]


def match_fitting_applicant(
    company: dict[str, Any], applicants: List[dict[str, Any]], take: int = 5
):
    company_sdt = company["sdt_profile"]
    return sorted(
        applicants,
        key=lambda applicant: mix_sdt(applicant["sdt_profile"], company_sdt),
        reverse=True,
    )[:take]
