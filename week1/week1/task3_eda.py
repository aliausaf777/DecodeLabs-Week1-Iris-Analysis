import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "iris_cleaned.csv"))

print("=" * 50)
print("TASK 3: Exploratory Data Analysis (EDA)")
print("=" * 50)
print("\n📊 Descriptive Statistics:")
print(df.describe().round(2).to_string())
print("\n📈 Mean per Species:")
print(df.groupby('species').mean().round(2).to_string())

num_cols = df.select_dtypes(include='number').columns
corr = df[num_cols].corr().round(2)
print("\n🔗 Correlation Matrix:")
print(corr.to_string())

print("\n🚨 Outliers (IQR method):")
for col in num_cols:
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    print(f"   {col}: {len(outliers)} outliers")

fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle("Iris EDA - Task 3", fontsize=16, fontweight='bold')
colors = ['#4CAF50', '#2196F3', '#FF9800']
species_list = df['species'].unique()

for sp, c in zip(species_list, colors):
    axes[0,0].hist(df[df['species']==sp]['petal length (cm)'], alpha=0.7, label=sp, color=c, bins=12)
axes[0,0].set_title('Petal Length Distribution')
axes[0,0].legend()

df.boxplot(column='sepal width (cm)', by='species', ax=axes[0,1])
axes[0,1].set_title('Sepal Width by Species')
plt.sca(axes[0,1]); plt.title('Sepal Width by Species')

for sp, c in zip(species_list, colors):
    sub = df[df['species']==sp]
    axes[1,0].scatter(sub['petal length (cm)'], sub['petal width (cm)'], label=sp, color=c, alpha=0.7)
axes[1,0].set_title('Petal Length vs Petal Width')
axes[1,0].legend()

sns.heatmap(corr, annot=True, fmt='.2f', cmap='Greens', ax=axes[1,1])
axes[1,1].set_title('Correlation Heatmap')

plt.tight_layout()
save_path = os.path.join(BASE_DIR, "iris_eda_charts.png")
plt.savefig(save_path, dpi=150, bbox_inches='tight')
print(f"\n✅ Chart saved to: {save_path}")

print("\n📝 Key Findings:")
print("   1. Setosa has distinctly smaller petals")
print("   2. Petal length & width are highly correlated (r ≈ 0.96)")
print("   3. Virginica has the largest petals overall")
print("   4. Sepal width has the most outliers")