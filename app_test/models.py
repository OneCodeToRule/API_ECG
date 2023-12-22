from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from app_test.database import Base

class ECG(Base):
    __tablename__ = "ecgs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    # Add other necessary fields (date, leads, signal, etc.)
