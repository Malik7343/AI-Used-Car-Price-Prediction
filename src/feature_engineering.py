from pathlib import Path

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


class FeatureEngineering:

    def __init__(self):

        self.dataset_path = (
            Path(__file__).resolve().parent.parent
            / "dataset"
            / "cleaned_cardekho_dataset.csv"
        )

    def prepare_features(self):

        # Load cleaned dataset
        df = pd.read_csv(self.dataset_path)

        # Features
        X = df.drop("selling_price", axis=1)

        # Target
        y = df["selling_price"]

        # Numerical Columns
        numerical_columns = X.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()

        # Categorical Columns
        categorical_columns = X.select_dtypes(
            include=["object"]
        ).columns.tolist()

        # One-Hot Encoder
        preprocessor = ColumnTransformer(
            transformers=[
                (
                    "categorical",
                    OneHotEncoder(handle_unknown="ignore"),
                    categorical_columns,
                )
            ],
            remainder="passthrough",
        )

        print("=" * 60)
        print("Feature Engineering Completed")
        print("=" * 60)

        print("\nFeatures Shape :", X.shape)
        print("Target Shape   :", y.shape)

        print("\nNumerical Columns")
        print(numerical_columns)

        print("\nCategorical Columns")
        print(categorical_columns)

        return X, y, preprocessor


if __name__ == "__main__":

    feature = FeatureEngineering()

    X, y, preprocessor = feature.prepare_features()