from fastapi import FastAPI # type: ignore

from server.routes.applicant import router as ApplicantRouter
from server.routes.company import router as CompanyRouter
from server.routes.matching import router as MatchingRouter

app = FastAPI() # type: ignore

app.include_router(ApplicantRouter, tags=["Applicant"], prefix="/applicant")
app.include_router(CompanyRouter, tags=["Company"], prefix="/company")
app.include_router(MatchingRouter, tags=["Matching"], prefix="/matching")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Mint! To access the API endpoints please visit /docs"}