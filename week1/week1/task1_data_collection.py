import pandas as pd
import os
from sklearn.datasets import load_iris

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("=" * 50)
print("TASK 1: Data Collection & Dataset Understanding")
print("=" * 50)
print(f"\n📦 Dataset: Iris Flower Dataset")
print(f"   150 iris flowers across 3 species: setosa, versicolor, virginica")
print(f"\n📐 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print("\n📋 Columns & Data Types:")
print(df.dtypes.to_string())
print("\n🔍 First 5 rows:")
print(df.head().to_string())
print("\n📊 Class Distribution:")
print(df['species'].value_counts().to_string())
print("\n📈 Basic Stats:")
print(df.describe().round(2).to_string())

save_path = os.path.join(BASE_DIR, "iris_dataset.csv")
df.to_csv(save_path, index=False)
print(f"\n✅ Saved to: {save_path}")