from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import CarInput
from app.predictor import Predictor

app = FastAPI(
    title="AI Used Car Price Prediction API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predictor = Predictor()


@app.get("/")
def home():
    return {
        "message": "AI Used Car Price Prediction API is Running!"
    }


@app.post("/predict")
def predict(car: CarInput):
    predicted_price = predictor.predict(car.model_dump())

    return {
        "predicted_price": round(predicted_price, 2)
    }