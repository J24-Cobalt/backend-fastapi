# API Documentation

## Applicant Endpoints

### Add Applicant
- **Endpoint:** `/applicant/`
- **Method:** `POST`
- **Description:** Adds a new applicant to the database.
- **Request Body:** 
  - `applicant`: `ApplicantSchema` (Required)

### Get Applicants
- **Endpoint:** `/applicant/`
- **Method:** `GET`
- **Description:** Retrieves all applicants.
- **Response:** List of applicants.

### Get Applicant by ID
- **Endpoint:** `/applicant/{id}`
- **Method:** `GET`
- **Description:** Retrieves a specific applicant by ID.
- **Path Parameter:**
  - `id`: `str` (Required)

### Update Applicant
- **Endpoint:** `/applicant/{id}`
- **Method:** `PUT`
- **Description:** Updates the information of a specific applicant.
- **Path Parameter:**
  - `id`: `str` (Required)
- **Request Body:** 
  - `applicant`: `UpdateApplicantModel` (Required)

### Delete Applicant
- **Endpoint:** `/applicant/{id}`
- **Method:** `DELETE`
- **Description:** Deletes a specific applicant by ID.
- **Path Parameter:**
  - `id`: `str` (Required)

## Company Endpoints

### Add Company
- **Endpoint:** `/company/`
- **Method:** `POST`
- **Description:** Adds a new company to the database.
- **Request Body:** 
  - `company`: `CompanySchema` (Required)

### Get Companies
- **Endpoint:** `/company/`
- **Method:** `GET`
- **Description:** Retrieves all companies.
- **Response:** List of companies.

### Get Company by ID
- **Endpoint:** `/company/{id}`
- **Method:** `GET`
- **Description:** Retrieves a specific company by ID.
- **Path Parameter:**
  - `id`: `str` (Required)

### Update Company
- **Endpoint:** `/company/{id}`
- **Method:** `PUT`
- **Description:** Updates the information of a specific company.
- **Path Parameter:**
  - `id`: `str` (Required)
- **Request Body:** 
  - `company`: `UpdateCompanyModel` (Required)

### Delete Company
- **Endpoint:** `/company/{id}`
- **Method:** `DELETE`
- **Description:** Deletes a specific company by ID.
- **Path Parameter:**
  - `id`: `str` (Required)


## Database Fields

### Applicant Database
- **ApplicantSchema**:
  - `fullname`: `str`
  - `username`: `str`
  - `password`: `str` (min_length=12)
  - `email`: `EmailStr`
  - `years_of_employment`: `Optional[int]`
  - `employment_status`: `str` (default="unemployed")
  - `age`: `Optional[int]` (ge=0)
  - `gender`: `Optional[str]` (pattern=r'^(Male|Female|Other)$')
  - `intro`: `Optional[str]` (max_length=250)
  - `avatar`: `Optional[str]`
  - `work_experience`: `Optional[List[WorkExperience]]`
    - `WorkExperience`:
      - `company`: `str`
      - `position`: `str`
      - `start_date`: `str`
      - `end_date`: `Optional[str]`
      - `description`: `Optional[str]`
  - `education`: `Optional[List[Education]]`
    - `Education`:
      - `institution`: `str`
      - `degree`: `str`
      - `start_date`: `str`
      - `end_date`: `Optional[str]`
      - `score`: `Optional[float]`
  - `skills`: `Optional[List[str]]`
  - `mental_profile`: `Optional[Dict[str, Any]]`
  - `cv`: `Optional[str]`
  - `applications`: `Optional[List[Dict[str, Any]]]`

### Company Database
- **CompanySchema**:
  - `name`: `str`
  - `email`: `EmailStr`
  - `password`: `str` (min_length=12)
  - `culture_metric`: `Dict[str, Any]`
  - `jobs`: `List[Job]`
    - `Job`:
      - `title`: `str`
      - `description`: `str`
      - `location`: `str`
  - `logo`: `Optional[str]`
  - `description`: `Optional[str]`
