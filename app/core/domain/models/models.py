from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    disabled: bool 
    role: str


class ECGLead(BaseModel):
    name: str
    number_of_samples: Optional[int]
    signal: List[int]


class ECG(BaseModel):
    id: int
    date: str
    leads: List[ECGLead]


class ECGInsights(BaseModel):
    ecg_id: int
    zero_crossings: int
