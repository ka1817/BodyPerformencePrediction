from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from database import engine, get_db
from sqlalchemy.orm import Session
import models  # Import models to create tables

# Ensure tables are created when FastAPI starts
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Load the trained model
model = joblib.load("random_forest_pipeline.pkl")

# Request model for prediction
class BodyPerformanceInput(BaseModel):
    age: int
    gender: int
    weight_kg: float
    body_fat: float = Field(..., alias="body fat_%")  # Fix name to match model
    diastolic: int
    sit_and_bend_forward_cm: float = Field(..., alias="sit and bend forward_cm")  
    sit_ups_counts: int = Field(..., alias="sit-ups counts")  
    broad_jump_cm: int

@app.post("/predict/")
def predict(data: BodyPerformanceInput, db: Session = Depends(get_db)):
    try:
        # Convert input data into DataFrame with correct column names
        input_data = pd.DataFrame([data.dict(by_alias=True)])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Save input to database
        db_record = models.BodyPerformance(**data.dict())
        db.add(db_record)
        db.commit()

        return {"prediction": prediction}
    
    except Exception as e:
        return {"error": str(e)}

# Root endpoint
@app.get("/")
def home():
    return {"message": "Body Performance Prediction API is running!"}
