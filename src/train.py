from pathlib import Path
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
)


class ModelTrainer:

    def __init__(self):

        self.dataset_path = (
            Path(__file__).resolve().parent.parent
            / "dataset"
            / "cleaned_cardekho_dataset.csv"
        )

        self.model_path = (
            Path(__file__).resolve().parent.parent
            / "models"
            / "used_car_price_model.joblib"
        )

    def train(self):

        # Load Dataset
        df = pd.read_csv(self.dataset_path)

        # Features & Target
        X = df.drop("selling_price", axis=1)
        y = df["selling_price"]

        # Columns
        categorical = X.select_dtypes(include="object").columns

        preprocessor = ColumnTransformer(
            transformers=[
                (
                    "cat",
                    OneHotEncoder(handle_unknown="ignore"),
                    categorical,
                )
            ],
            remainder="passthrough",
        )

        # Train/Test Split
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
        )

        # Models
        models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(random_state=42),
            "Random Forest": RandomForestRegressor(
                n_estimators=200,
                random_state=42,
            ),
            "Gradient Boosting": GradientBoostingRegressor(
                random_state=42,
            ),
        }

        results = []

        best_model = None
        best_score = -1

        print("=" * 60)
        print("Training Models...")
        print("=" * 60)

        for name, model in models.items():

            pipeline = Pipeline([
                ("preprocessor", preprocessor),
                ("model", model),
            ])

            pipeline.fit(X_train, y_train)

            predictions = pipeline.predict(X_test)

            mae = mean_absolute_error(y_test, predictions)
            rmse = mean_squared_error(
                y_test,
                predictions
            ) ** 0.5
            r2 = r2_score(y_test, predictions)

            results.append({
                "Model": name,
                "MAE": round(mae, 2),
                "RMSE": round(rmse, 2),
                "R2 Score": round(r2, 4),
            })

            if r2 > best_score:
                best_score = r2
                best_model = pipeline

        # Results
        results_df = pd.DataFrame(results)

        print("\nModel Comparison\n")
        print(results_df.sort_values(
            by="R2 Score",
            ascending=False
        ))

        # Save Best Model
        joblib.dump(best_model, self.model_path)

        print("\nBest Model Saved Successfully!")
        print(self.model_path)


if __name__ == "__main__":

    trainer = ModelTrainer()

    trainer.train()