from typing import List

from pydantic import BaseModel

from app.domain.models.ecg_lead import ECGLead


class ECG(BaseModel):
    id: int
    date: str
    leads: List[ECGLead]
