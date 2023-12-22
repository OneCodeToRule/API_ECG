from fastapi import FastAPI
from app.api.endpoints import authentication

from app.api.endpoints import ecg


app = FastAPI()
app.include_router(authentication.router)
app.include_router(ecg.router)