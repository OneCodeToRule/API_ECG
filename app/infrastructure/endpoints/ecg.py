from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from app.application.ecg_service import ECGNotFoundException, add_ecg, get_insights_by_ecg_id

from app.application.auth_service import oauth2_scheme
from app.domain.models import ECG, User


router = APIRouter()


@router.post("/upload_ecg/", response_model=ECG)
async def upload_ecg(ecg: ECG, token: str = Depends(oauth2_scheme)):
    result = add_ecg(ecg)
    return result


@router.get("/get_ecg_insights_by_ecg_id/{ecg_id}")
async def get_ecg_insights_by_ecg_id(ecg_id: int, current_user: User = Depends(oauth2_scheme)):
    try:
        return get_insights_by_ecg_id(ecg_id)
    except ECGNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
