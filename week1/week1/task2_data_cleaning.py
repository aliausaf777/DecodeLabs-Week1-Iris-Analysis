import pandas as pd
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "iris_dataset.csv"))

df_messy = df.copy()
np.random.seed(42)
for col in df_messy.columns[:4]:
    idx = np.random.choice(df_messy.index, 5, replace=False)
    df_messy.loc[idx, col] = np.nan
df_messy = pd.concat([df_messy, df_messy.sample(5, random_state=1)], ignore_index=True)

print("=" * 50)
print("TASK 2: Data Cleaning & Preprocessing")
print("=" * 50)
print(f"\n🔴 BEFORE Cleaning:")
print(f"   Rows: {len(df_messy)}")
print(f"   Missing values:\n{df_messy.isnull().sum().to_string()}")
print(f"   Duplicates: {df_messy.duplicated().sum()}")

df_clean = df_messy.drop_duplicates()
num_cols = df_clean.select_dtypes(include='number').columns
for col in num_cols:
    median_val = df_clean[col].median()
    missing = df_clean[col].isnull().sum()
    df_clean[col] = df_clean[col].fillna(median_val)
    if missing > 0:
        print(f"   Filled {missing} missing in '{col}' with median ({median_val:.2f})")

df_clean[num_cols] = df_clean[num_cols].round(2)
df_clean['species'] = df_clean['species'].astype(str).str.strip().str.lower()

print(f"\n✅ AFTER Cleaning:")
print(f"   Rows: {len(df_clean)}")
print(f"   Missing values: {df_clean.isnull().sum().sum()}")
print(f"   Duplicates: {df_clean.duplicated().sum()}")

save_path = os.path.join(BASE_DIR, "iris_cleaned.csv")
df_clean.to_csv(save_path, index=False)
print(f"\n✅ Saved to: {save_path}")