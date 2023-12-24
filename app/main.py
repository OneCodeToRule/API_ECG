from fastapi import FastAPI
from app.infrastructure.endpoints import authentication, ecg


app = FastAPI()
app.include_router(authentication.router)
app.include_router(ecg.router)
