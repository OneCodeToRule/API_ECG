from typing import List, Optional

from pydantic import BaseModel


class ECGLead(BaseModel):
    name: str
    number_of_samples: Optional[int]
    signal: List[int]
