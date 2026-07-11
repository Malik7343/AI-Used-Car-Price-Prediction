from pathlib import Path
import joblib
import pandas as pd


class Predictor:

    def __init__(self):

        model_path = (
            Path(__file__).resolve().parent.parent
            / "models"
            / "used_car_price_model.joblib"
        )

        print("Loading Model...")
        self.model = joblib.load(model_path)
        print("Model Loaded Successfully!")

    def predict(self, car_data: dict):

        df = pd.DataFrame([car_data])

        prediction = self.model.predict(df)

        return float(prediction[0])