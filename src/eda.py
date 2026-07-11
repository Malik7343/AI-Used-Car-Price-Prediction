from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class EDA:

    def __init__(self):

        self.dataset_path = (
            Path(__file__).resolve().parent.parent
            / "dataset"
            / "cleaned_cardekho_dataset.csv"
        )

        self.report_path = (
            Path(__file__).resolve().parent.parent
            / "reports"
        )

        self.report_path.mkdir(exist_ok=True)

    def run(self):

        df = pd.read_csv(self.dataset_path)

        print("=" * 60)
        print("Exploratory Data Analysis")
        print("=" * 60)

        print("\nShape")
        print(df.shape)

        print("\nData Types")
        print(df.dtypes)

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nStatistics")
        print(df.describe())

        # ----------------------------
        # Selling Price Distribution
        # ----------------------------

        plt.figure(figsize=(10,5))
        sns.histplot(df["selling_price"], bins=40, kde=True)

        plt.title("Selling Price Distribution")

        plt.savefig(
            self.report_path / "selling_price_distribution.png"
        )

        plt.close()

        # ----------------------------
        # Correlation Heatmap
        # ----------------------------

        plt.figure(figsize=(10,8))

        sns.heatmap(
            df.select_dtypes(include="number").corr(),
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Correlation Heatmap")

        plt.savefig(
            self.report_path / "correlation_heatmap.png"
        )

        plt.close()

        # ----------------------------
        # Brand Distribution
        # ----------------------------

        plt.figure(figsize=(12,8))

        sns.countplot(
            y=df["brand"],
            order=df["brand"].value_counts().index
        )

        plt.title("Brand Distribution")

        plt.savefig(
            self.report_path / "brand_distribution.png"
        )

        plt.close()

        print("\nEDA Completed Successfully!")
        print("Reports Saved In:", self.report_path)


if __name__ == "__main__":

    eda = EDA()

    eda.run()