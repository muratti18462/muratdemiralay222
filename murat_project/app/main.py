from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class PredictionInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict")
def predict(input_data: PredictionInput):
    pred_class = predict_pipeline(input_data.text)
    return {"predicted_class": pred_class}