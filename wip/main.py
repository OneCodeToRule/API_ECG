from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from wip import models, schemas, database

app = FastAPI()

# Database initialization
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to upload ECG
@app.post("/upload_ecg/")
def upload_ecg(ecg: schemas.ECGCreate, db: Session = Depends(get_db)):
    # Save the ECG to the database
    db_ecg = models.ECG(**ecg.dict())
    db.add(db_ecg)
    db.commit()
    db.refresh(db_ecg)
    return {"message": "ECG received and processed successfully"}

# Endpoint to get ECG insights
@app.get("/ecg_insights/{user_id}")
def get_ecg_insights(user_id: int, db: Session = Depends(get_db)):
    # Retrieve ECGs from the database for the user
    user_ecgs = db.query(models.ECG).filter(models.ECG.user_id == user_id).all()
    # Perform calculations for insights
    # Return insights
    return {"insights": "Insights for user's ECGs"}
