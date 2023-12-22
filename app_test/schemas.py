from pydantic import BaseModel, List

class Lead(BaseModel):
    name: str
    number_of_samples: int
    signal: List[int]

class ECGBase(BaseModel):
    id: int
    user_id: int
    # Add other necessary fields (date, leads, signal, etc.)

class ECGCreate(ECGBase):
    pass
