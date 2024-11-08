from fastapi import FastAPI # type: ignore

from server.routes.applicant import router as ApplicantRouter # type: ignore

app = FastAPI() # type: ignore

app.include_router(ApplicantRouter, tags=["Applicant"], prefix="/applicant")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}