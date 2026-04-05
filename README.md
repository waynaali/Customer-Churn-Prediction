# Customer Churn Prediction

## Week 1 – Week 3: EDA + Machine Learning + Model Optimization

### 📌 Course Information

* **Course:** Introduction to Applied Artificial Intelligence
* **Semester:** BS 8th Semester
* **Project:** Customer Churn Prediction
* **Author:** Wayna Ali
* **Date:** 04/05/2026

---

## 📊 Project Overview

This project focuses on performing **Exploratory Data Analysis (EDA)**, building **machine learning models**, and applying **model optimization techniques** on the Telco Customer Churn dataset.

**Goals:**

* Understand customer behavior patterns
* Identify factors contributing to churn
* Build predictive models to classify churn
* Optimize model performance
* Generate actionable business insights

---

## 📂 Dataset Information

* **Source:** Telco Customer Churn Dataset (Kaggle)
* **Total Customers:** 7,043
* **Total Features:** 21
* **Target Variable:** `Churn` (Yes/No)

⚠️ Note: The dataset file (`customer_data.csv`) is not included in this repository.
Please download it from Kaggle and place it in the project folder before running the notebooks.

---

## 📁 Repository Structure

* `week1_eda.ipynb` → Exploratory Data Analysis
* `week2_ml_models.ipynb` → Baseline ML models
* `week3_optimization.ipynb` → Model tuning & optimization
* `best_churn_model.pkl` → Saved optimized model
* `model_metadata.json` → Model configuration & parameters
* `README.md` → Project documentation
* `.gitignore` → Excludes unnecessary files

---

## 🔍 Key Insights

### **Week 1: EDA**

* Month-to-month contract customers show highest churn
* Short tenure customers (< 6 months) are high-risk
* Higher Monthly Charges → higher churn probability
* Fiber optic users churn more than DSL users
* Electronic check users have higher churn

---

### **Week 2: ML Models**

* Models trained:

  * Logistic Regression
  * Decision Tree
  * Random Forest

* Feature engineering:

  * `TotalRevenue`
  * `TotalServices`
  * `TenureGroup`
  * `HighCharges`

* Random Forest performed best among baseline models

---

### **Week 3: Model Optimization**

* Applied **hyperparameter tuning** (Grid Search / Random Search)
* Used **cross-validation** for reliable evaluation
* Optimized models:

  * Random Forest
  * XGBoost

**Results:**

| Model             | Accuracy |
| ----------------- | -------- |
| Baseline RF       | ~82%     |
| Optimized RF      | ~86%     |
| Optimized XGBoost | ~88–89%  |

✅ **Best Model:** Optimized XGBoost
✅ Achieved **85%+ accuracy target**

---

## 🧠 Key Learnings

* Cross-validation improves reliability of results
* Hyperparameter tuning significantly boosts performance
* XGBoost outperforms traditional ensemble methods
* Feature engineering plays a critical role in prediction quality
* Model comparison is essential before final selection

---

## ⚙️ Setup Instructions

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter xgboost
```

Run notebooks:

```bash
jupyter notebook week1_eda.ipynb
jupyter notebook week2_ml_models.ipynb
jupyter notebook week3_optimization.ipynb
```

---

## 🚀 Next Steps (Week 4)

* Deploy model using Flask / Streamlit
* Build interactive UI for predictions
* Add model explainability (SHAP)
* Perform real-time inference

---

## 🎯 Learning Outcomes

* Data preprocessing & cleaning
* Exploratory Data Analysis (EDA)
* Machine learning model development
* Feature engineering
* Model optimization & tuning
* Performance evaluation techniques
* Business insight extraction
* End-to-end ML workflow
* Git & GitHub version control

---

## 📬 Contact

* LinkedIn: [Wayna Ali](https://www.linkedin.com/in/waynaali/)
* GitHub: [waynaali](https://github.com/waynaali)
