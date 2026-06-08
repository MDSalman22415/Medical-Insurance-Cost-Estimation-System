# Medical Insurance Cost Prediction

<img src="Project baner.png" width="1000">

## 📌 Project Overview

The Medical Insurance Cost Prediction System is a Machine Learning project that predicts a customer's medical insurance charges based on factors such as age, BMI, smoking status, number of children, gender, and region.

The project includes:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Building
- Model Evaluation
- Insurance Cost Prediction

---

## 📊 Dataset Information

The dataset contains the following features:

| Feature | Description |
|----------|------------|
| Age | Age of the customer |
| Sex | Gender of the customer |
| BMI | Body Mass Index |
| Children | Number of dependents |
| Smoker | Smoking status |
| Region | Residential region |
| Charges | Medical insurance charges |

Dataset Size: **50,000 Records**

---

# 🔍 Exploratory Data Analysis (EDA)

## 1️⃣ Impact of Smoking on Insurance Charges

### Key Insight

Smoking has a significant impact on medical insurance costs.

- Smokers have substantially higher insurance charges.
- Non-smokers generally pay much lower insurance premiums.
- Smoking is one of the strongest factors affecting insurance costs.

### Visualization

<img src="Smoke vs Insurance charges images" width="1000">

---

## 2️⃣ Impact of Age on Insurance Charges

### Key Insight

Insurance charges increase as age increases.

- Teen customers have the lowest average charges.
- Senior customers have the highest average charges.
- Medical expenses tend to rise with age.

### Visualization

<img src="Age vs insurance charges" width="1000">

---

## 3️⃣ Impact of BMI on Insurance Charges

### Key Insight

Customers with higher BMI tend to incur higher insurance charges.

- Underweight customers have the lowest average charges.
- Obese customers have the highest average charges.
- Insurance costs generally increase as BMI category increases.

### Visualization

<img src="" width="1000">

---

## 4️⃣ Regional Analysis

### Key Insight

Insurance charges remain relatively similar across all regions.

- Northwest region shows the highest average charges.
- Southeast region shows the lowest average charges.
- Region has a limited impact compared to Age, BMI, and Smoking Status.

### Visualization

<img src="" width="1000">

---

## 5️⃣ Correlation Analysis

### Key Insight

Among numerical features:

- Age has the strongest correlation with insurance charges.
- BMI has a weak positive correlation.
- Number of children has minimal impact.
- Smoking remains the most influential factor overall.

### Visualization

<img src="" width="1000">

---

# 🤖 Machine Learning Models

Three regression models were trained and evaluated:

## 1. Linear Regression

Linear Regression was used as the baseline model to establish a relationship between customer attributes and insurance charges.

### Performance

- R² Score: **0.8998**
- Mean Cross Validation Score: **0.8982**

---

## 2. Lasso Regression

Lasso Regression applies L1 Regularization which helps reduce overfitting and can perform feature selection.

### Performance

- R² Score: **0.8998**
- Mean Cross Validation Score: **0.8982**

---

## 3. Ridge Regression

Ridge Regression applies L2 Regularization and helps stabilize coefficient values.

### Performance

- R² Score: **0.8998**
- Mean Cross Validation Score: **0.8982**

---

# 📈 Model Comparison

| Model | R² Score |
|---------|---------|
| Linear Regression | 0.8998 |
| Lasso Regression | 0.8998 |
| Ridge Regression | 0.8998 |

### Conclusion

All three models achieved nearly identical performance.

Ridge Regression achieved the highest score by a very small margin, indicating that the dataset is already well-structured and does not suffer significantly from overfitting.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook

---

# 🚀 Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Prediction System Development

---

# 🎯 Business Insights

- Smoking status is the most influential factor affecting insurance charges.
- Older customers tend to pay higher premiums.
- Higher BMI is associated with higher medical costs.
- Regional differences have minimal impact on charges.
- Machine Learning can accurately estimate insurance costs with nearly 90% prediction accuracy.

---

## Author

**Salman**
Machine Learning & Data Science Enthusiast
