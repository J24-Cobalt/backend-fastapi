from fastapi import FastAPI # type: ignore

from server.routes.applicant import router as ApplicantRouter
from server.routes.company import router as CompanyRouter
from server.routes.matching import router as MatchingRouter
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
]

app = FastAPI() # type: ignore

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(ApplicantRouter, tags=["Applicant"], prefix="/applicant")
app.include_router(CompanyRouter, tags=["Company"], prefix="/company")
app.include_router(MatchingRouter, tags=["Matching"], prefix="/matching")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Mint! To access the API endpoints please visit /docs"}