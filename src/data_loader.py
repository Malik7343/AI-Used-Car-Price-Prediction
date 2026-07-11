from pathlib import Path
import pandas as pd


class DataLoader:
    """
    Load dataset from the dataset folder.
    """

    def __init__(self):
        self.dataset_path = (
            Path(__file__).resolve().parent.parent
            / "dataset"
            / "cardekho_dataset.csv"
        )

    def load_data(self):

        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.dataset_path}"
            )

        df = pd.read_csv(self.dataset_path)

        return df


if __name__ == "__main__":

    loader = DataLoader()

    df = loader.load_data()

    print("=" * 50)
    print("Dataset Loaded Successfully")
    print("=" * 50)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())