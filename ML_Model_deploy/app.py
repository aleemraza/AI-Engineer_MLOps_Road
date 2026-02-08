import time
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from logging_config import logger

app = FastAPI(title="ML Model API")

# Load trained model
model = joblib.load("model.pkl")

class PredictInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    
class PredictOutput(BaseModel):
    prediction: int    
    
    
@app.get("/health")
def health():
    return {"status": "ok"}


# Metrics endpoint

REQUEST_COUNT = 0

@app.get("/metrics")
def metrics():
    return {
        "requests_total": REQUEST_COUNT
    }
    
    
@app.post("/predict", response_model=PredictOutput)
def predict(data: PredictInput):
    start = time.time()
    X = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    pred = model.predict(X)[0]
    latency = round(time.time() - start, 4)
    logger.info(f"Prediction={pred} latency={latency}s")
    return {"prediction": int(pred), "latency": latency} 

@app.get("/")
def root():
    return {"message": "ML service is running"} 