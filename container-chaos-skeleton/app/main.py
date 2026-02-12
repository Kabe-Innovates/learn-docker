from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# 1. Define the input data format (The "Contract")
class ModelInput(BaseModel):
    feature1: float
    feature2: float

# 2. The Prediction Endpoint
@app.post("/predict")
def predict(data: ModelInput):
    # SIMULATION: In the real event, you'd load a model here.
    # For now, we return a random fake prediction.
    result = data.feature1 * random.random()
    
    return {"prediction": result, "status": "success"}

# 3. Health Check (CRITICAL for Docker)
@app.get("/health")
def health():
    return {"status": "alive"}