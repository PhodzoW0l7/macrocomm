from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.incidents import incidentRouter

app=FastAPI()

app.include_router(incidentRouter, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {
        "message":"Welcome to my FastAPI & Angular Fullstack Application"
    }


