def match_fitting_company(applicant, companies):
    with open("sample_entry_companies.txt", "w") as file:
        for company in companies:
            file.write(str(company) + "\n")
    return companies[0]


def match_fitting_applicant(company, applicants):
    with open("sample_entry_applicants.txt", "w") as file:
        for applicant in applicants:
            file.write(str(applicant) + "\n")
    return applicants[0]

