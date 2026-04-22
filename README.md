# IABAC-Employee-Performance# 
# Employee Performance Prediction System

##  Project Overview

This project aims to predict employee performance ratings using Machine Learning techniques.
The model analyzes various factors such as job role, work environment, experience, and salary hike to determine performance levels.

---

##  Problem Statement

Organizations often struggle to evaluate employee performance effectively.
This project helps in predicting employee performance based on historical data, enabling better HR decision-making.

---

##  Dataset Information

* Total Records: **1200**
* Total Features: **28**
* Target Variable: **PerformanceRating**

### Key Features:

* Age
* Department
* Job Role
* Work Experience
* Environment Satisfaction
* Salary Hike Percentage
* Work-Life Balance

---

##  Data Preprocessing

* No missing values found
* Categorical variables encoded
* Feature selection performed
* Handled class imbalance using **SMOTE**

---

##  Exploratory Data Analysis

* Performance rating distribution analyzed
* Correlation heatmap created
* Key insights derived from employee satisfaction and salary factors

---

##  Model Building

* Algorithm Used: **Random Forest Classifier**
* Train-Test Split: 80-20
* Why Random Forest:

  * Handles non-linear relationships
  * Works well with mixed data types
  * Robust and less prone to overfitting

---

##  Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | ~93%  |
| Precision | High  |
| Recall    | Good  |

### Key Observations:

* Class 3 (Average Performance) predicted most accurately
* Class 4 slightly lower recall due to imbalance

---

##  Feature Importance

Top factors affecting performance:

* EmpLastSalaryHikePercent
* EmpEnvironmentSatisfaction
* YearsSinceLastPromotion

### Insight:

Employees with higher salary growth and better work environment tend to perform better.

---

##  Deployment

The model is deployed using Streamlit and accessible via a web interface.

 **Live App:**
 https://aditya-employee-performance.streamlit.app/

---

##  Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

##  Screenshots

*![Screenshot of my app](<Screenshot 2026-04-22 223104.png>)*

---

##  Conclusion

The model successfully predicts employee performance with high accuracy and provides valuable insights for HR analytics.

---

##  Future Improvements

* Improve performance for minority classes
* Use advanced models like XGBoost
* Integrate real-time HR data

---

## 👨 Author

### Aditya Motghare

AI-powered Employee Performance Prediction System using Machine Learning, built as part of IABAC certification. Includes EDA, feature engineering, and a Streamlit web app for real-time predictions.
