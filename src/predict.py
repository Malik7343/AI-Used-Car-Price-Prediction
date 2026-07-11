from pathlib import Path
import joblib
import pandas as pd


class CarPricePredictor:

    def __init__(self):

        print("Loading Model...")

        self.model_path = (
            Path(__file__).resolve().parent.parent
            / "models"
            / "used_car_price_model.joblib"
        )

        if not self.model_path.exists():
            raise FileNotFoundError(f"Model not found: {self.model_path}")

        self.model = joblib.load(self.model_path)

        print("Model Loaded Successfully!")

    def predict(self):

        print("Preparing Input Data...")

        car = pd.DataFrame([
            {
                "car_name": "Maruti Alto",
                "brand": "Maruti",
                "model": "Alto",
                "vehicle_age": 5,
                "km_driven": 50000,
                "seller_type": "Dealer",
                "fuel_type": "Petrol",
                "transmission_type": "Manual",
                "mileage": 21,
                "engine": 998,
                "max_power": 67.1,
                "seats": 5
            }
        ])

        print("Making Prediction...")

        prediction = self.model.predict(car)

        print("\n" + "=" * 50)
        print("USED CAR PRICE PREDICTION")
        print("=" * 50)

        print("\nInput Car Details")
        print(car)

        print(f"\nEstimated Selling Price: ₹ {prediction[0]:,.2f}")

        print("=" * 50)


if __name__ == "__main__":

    print("Predict.py Started...\n")

    predictor = CarPricePredictor()

    predictor.predict()

    print("\nPrediction Completed Successfully!")