from pydantic import BaseModel


class ECGInsights(BaseModel):
    ecg_id: int
    zero_crossings: int
