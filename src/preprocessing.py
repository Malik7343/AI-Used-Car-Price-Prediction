from pathlib import Path
import pandas as pd

from data_loader import DataLoader


class DataPreprocessor:

    def __init__(self):

        self.loader = DataLoader()

        self.output_path = (
            Path(__file__).resolve().parent.parent
            / "dataset"
            / "cleaned_cardekho_dataset.csv"
        )

    def preprocess(self):

        df = self.loader.load_data()

        # Remove unnecessary column
        df.drop(columns=["Unnamed: 0"], errors="ignore", inplace=True)

        # Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # Check missing values
        missing = df.isnull().sum()

        print("\nMissing Values")
        print(missing)

        print("\nDataset Shape After Cleaning")
        print(df.shape)

        # Save cleaned dataset
        df.to_csv(self.output_path, index=False)

        print("\nClean dataset saved successfully!")
        print(self.output_path)

        return df


if __name__ == "__main__":

    processor = DataPreprocessor()

    processor.preprocess()