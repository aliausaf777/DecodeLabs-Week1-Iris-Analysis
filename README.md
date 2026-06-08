# 🌸 Iris Flower Dataset — Data Science Project
### Decodelabs Data Science Internship | Week 1 Task Submission

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4c72b0?style=flat)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-4a7c59?style=flat)

---

## 📋 Overview

This project was completed as part of the **Decodelabs Data Science Internship — Week 1**. It walks through the full beginner data science pipeline using the classic **Iris Flower Dataset**: from loading and understanding raw data, to cleaning it, to performing a complete exploratory data analysis with visualizations.

The Iris dataset contains measurements of 150 flowers across 3 species — *Setosa*, *Versicolor*, and *Virginica* — and is one of the most well-known datasets in data science and machine learning.

---

## ✅ Tasks Completed

| # | Task | Description |
|---|------|-------------|
| 1 | **Data Collection & Dataset Understanding** | Loaded dataset, identified columns, data types, shape, and missing values |
| 2 | **Data Cleaning & Preprocessing** | Handled missing values, removed duplicates, formatted and exported clean data |
| 3 | **Exploratory Data Analysis (EDA)** | Computed statistics, identified trends and outliers, generated visualizations |

---

## 📁 Project Structure

```
decodelabs_tasks1/
│
├── week1/
│   ├── task1_data_collection.py   # Task 1 — Data loading & understanding
│   ├── task2_data_cleaning.py     # Task 2 — Cleaning & preprocessing
│   ├── task3_eda.py               # Task 3 — EDA & visualizations
│   ├── iris_dataset.csv           # Original raw dataset
│   ├── iris_cleaned.csv           # Cleaned dataset output
│   └── iris_eda_charts.png        # EDA visualization output
│
└── README.md
```

---

## 🗂️ Dataset

- **Name:** Iris Flower Dataset
- **Source:** Scikit-learn built-in (`load_iris()`)
- **Shape:** 150 rows × 5 columns
- **Classes:** Setosa, Versicolor, Virginica (50 samples each)

### Columns

| Column | Type | Description |
|--------|------|-------------|
| `sepal_length` | float | Sepal length in cm |
| `sepal_width` | float | Sepal width in cm |
| `petal_length` | float | Petal length in cm |
| `petal_width` | float | Petal width in cm |
| `species` | string | Flower species (target) |

---

## 🧹 Task 2: Cleaning Steps

1. **Checked for missing values** — none found, dataset is clean by nature
2. **Checked for duplicates** — identified and removed duplicate rows
3. **Verified data types** — all numeric columns confirmed as `float64`
4. **Exported clean data** — saved as `iris_cleaned.csv` for use in Task 3

---

## 📊 Task 3: Key Findings

> **The three species are clearly distinguishable — especially by petal measurements.**

| Finding | Detail |
|---------|--------|
| 🌸 Setosa | Has significantly smaller petals — easily separable from the other two species |
| 📏 Petal correlation | Petal Length and Petal Width are highly correlated (r ≈ **0.96**) |
| 🌺 Virginica | Generally has the largest petals of all three species |
| 📉 Sepal Width | Shows the most variation and outliers across all species |
| 🎯 Best feature | Petal measurements are far more useful for classification than sepal measurements |

---

## 📈 Visualizations

The script generates a multi-panel EDA chart saved as `iris_eda_charts.png` including:

- Distribution plots per feature
- Pairplot showing species separation
- Correlation heatmap
- Boxplots for outlier detection per species

![iris_eda_charts](week1/iris_eda_charts.png)

---

## ▶️ How to Run

**1. Clone the repo**
```bash
git clone https://github.com/aliausaf777/decodelabs_tasks1.git
cd decodelabs_tasks1/week1
```

**2. Install dependencies**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

**3. Run tasks in order**
```bash
python task1_data_collection.py
python task2_data_cleaning.py
python task3_eda.py
```

Each script prints results to the console. Task 3 also saves `iris_eda_charts.png` automatically.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Pandas** — data manipulation and cleaning
- **NumPy** — numerical computations
- **Matplotlib** — custom visualizations
- **Seaborn** — statistical plotting
- **Scikit-learn** — dataset loading

---

## 👤 Author

**Ali**
B.Tech CSE (Data Science & AI) — Aurora Higher Education and Research Academy (JNTU Hyderabad)
Tech Lead, DataWizards Community

---

## 🏢 Internship

**Organization:** [Decodelabs](https://www.decodelabs.tech)
**Program:** Data Science Internship — Week 1 Task
**Tasks Submitted:** Task 1 · Task 2 · Task 3
