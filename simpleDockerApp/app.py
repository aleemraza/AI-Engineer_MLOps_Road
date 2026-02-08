from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="ML Inference API", version="1.0.0")

# ---------- Health Check ----------
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow()
    }

# ---------- Input Schema ----------
class PredictInput(BaseModel):
    age: int = Field(..., gt=0)
    bmi: float = Field(..., gt=0)
    glucose: float = Field(..., gt=0)

# ---------- Output Schema ----------
class PredictOutput(BaseModel):
    risk_score: float
    prediction: str


def predict(data: PredictInput):
    """
    Dummy prediction logic (replace with ML model later)
    """
    risk_score = (data.age * 0.2) + (data.bmi * 0.3) + (data.glucose * 0.5)

    prediction = "High Risk" if risk_score > 100 else "Low Risk"

    return PredictOutput(
        risk_score=round(risk_score, 2),
        prediction=prediction
    )    
    
# ---------- Prediction Endpoint ----------
@app.post("/predict", response_model=PredictOutput)    

# ---------- Root ----------
@app.get("/")
def root():
    return {"message": "FastAPI ML service is running 🚀"}
