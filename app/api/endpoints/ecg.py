from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth import decode_token, oauth2_scheme

from app.core.domain.models.models import ECG, ECGInsights, User


router = APIRouter()


@router.post("/upload_ecg/", response_model=ECG)
async def upload_ecg(ecg: ECG, token: str = Depends(oauth2_scheme)):
    return ecg


@router.get("/ecg_insights/{user_id}")
async def get_ecg_insights(user_id: int, current_user: User = Depends(decode_token)):
    # Lógica para obtener información del ECG y calcular los cruces por cero
    # Replace 10 with the actual zero crossings count
    return {"insights": {"ecg_id": "test", "zero_crossings": 10}}


@router.get("/get_insights/{ecg_id}", response_model=ECGInsights)
def get_insights(ecg_id: int):
    # Lógica para calcular los zero crossings
    # Supongamos que obtenemos el ECG almacenado con el ID proporcionado
    selected_ecg = next((ecg for ecg in stored_ecgs if ecg.id == ecg_id), None)
    if selected_ecg:
        zero_crossings = sum(abs(selected_ecg.leads[i].signal[j]) > 0 and abs(
            selected_ecg.leads[i].signal[j + 1]) > 0 for i in range(len(selected_ecg.leads)) for j in range(len(selected_ecg.leads[i].signal) - 1))
        return {"ecg_id": ecg_id, "zero_crossings": zero_crossings}
    else:
        # Si el ECG no se encuentra, se retorna cero cruces por cero
        return {"ecg_id": ecg_id, "zero_crossings": 0}
