# 💼 Salary Prediction Using Machine Learning

## 🚀 Live Demo

Experience the Salary Prediction System through the interactive Streamlit web application.

🌐 **Live Application:**  
🔗 https://mlprojectp19-hdbfn8anguoftpumgrzbrl.streamlit.app/

The application enables users to enter relevant employee and job-related details to receive **real-time salary predictions** powered by a trained **Machine Learning Regression model**. Built with **Python**, **Scikit-learn**, and **Streamlit**, the system provides an intuitive interface for instant salary estimation and demonstrates an end-to-end machine learning workflow from data preprocessing to deployment.

### ✨ Features

- 💼 Predict employee salaries in real time
- 🤖 Machine Learning-based regression model
- 📊 Fast and accurate salary estimation
- 🌐 Interactive and user-friendly Streamlit interface
- ⚡ Instant predictions with minimal input
- 📱 Accessible from any modern web browser

> **Try the live application and explore how Machine Learning can accurately estimate salaries based on user-provided information.**

---

# 📌 Project Overview

The **Data Science Salary Prediction System** is an **End-to-End Machine Learning Regression** project designed to predict employee salaries based on professional and organizational factors such as **experience level**, **employment type**, **job title**, **remote work ratio**, **employee residence**, **company location**, and **company size**.

The project leverages historical salary data from professionals working in **Data Science**, **Machine Learning**, **Artificial Intelligence**, **Data Engineering**, and **Business Analytics** to develop predictive models capable of estimating salaries with high accuracy. The dataset undergoes comprehensive **data cleaning**, **preprocessing**, **feature engineering**, and **exploratory data analysis (EDA)** before training multiple regression algorithms.

Several Machine Learning models are trained, evaluated, and compared using industry-standard regression metrics to identify the most accurate model. The final model is deployed through an interactive **Streamlit web application**, enabling users to enter job-related information and receive instant salary predictions.

This project demonstrates practical expertise in **Python**, **Data Analytics**, **Machine Learning**, **Regression Modeling**, **Feature Engineering**, **Model Evaluation**, and **Web Deployment**, making it an excellent portfolio project for aspiring **Machine Learning Engineers**, **Data Scientists**, **Python Developers**, and **AI Engineers**.

---

## ✨ Key Features

- 💼 Predict salaries using job and company-related information
- 📊 Data Cleaning, Preprocessing, and Feature Engineering
- 📈 Exploratory Data Analysis (EDA)
- 🤖 Multiple Machine Learning Regression Models
- 📏 Model Evaluation using MAE, MSE, RMSE, and R² Score
- 💾 Model Serialization using Pickle
- 🌐 Interactive Streamlit Web Application
- ☁️ Deployment Ready
- 🔗 Version Control with Git & GitHub
  
---

# 💡 Why Choose This Project?

Salary prediction is a real-world business problem that helps organizations make informed compensation decisions while enabling professionals to understand salary trends across the **Data Science**, **Machine Learning**, **Artificial Intelligence**, and **Analytics** industries.

This project demonstrates how **Machine Learning Regression** can analyze historical salary data to estimate employee salaries based on various professional and organizational factors. It provides valuable insights for **HR Analytics**, **workforce planning**, **salary benchmarking**, and **data-driven decision-making**.

### ⭐ Why I Chose This Project

- 💼 Explore real-world salary prediction and HR Analytics.
- 📊 Work with a real-world Data Science salary dataset.
- 🧹 Practice data cleaning, preprocessing, and feature engineering.
- 📈 Perform Exploratory Data Analysis (EDA) to uncover salary trends.
- 🤖 Implement and compare multiple Machine Learning regression models.
- 📏 Evaluate model performance using MAE, MSE, RMSE, and R² Score.
- 🌐 Build and deploy an interactive Streamlit web application.
- 🚀 Develop an end-to-end Machine Learning solution from data collection to deployment.
- 💻 Strengthen practical skills in Python, Data Analytics, Machine Learning, and Model Deployment for real-world business applications.

---

# 🎯 Project Objectives

The primary objective of this project is to develop an intelligent **Machine Learning Regression** system capable of accurately predicting employee salaries based on professional and organizational attributes. The project applies data analytics and predictive modeling techniques to support salary estimation and data-driven decision-making in Human Resource Analytics.

### ⭐ Key Objectives

- 💼 Predict employee salaries using Machine Learning regression algorithms.
- 📊 Analyze the key factors influencing salary, such as experience level, job title, employment type, company size, remote work ratio, and location.
- 🧹 Perform comprehensive data cleaning, preprocessing, and feature engineering.
- 📈 Conduct Exploratory Data Analysis (EDA) to identify salary trends and patterns.
- 🤖 Train and compare multiple Machine Learning regression models.
- 📏 Evaluate model performance using MAE, MSE, RMSE, and R² Score.
- 💾 Save the best-performing model for future predictions using Pickle.
- 🌐 Develop an interactive Streamlit web application for real-time salary prediction.
- 🚀 Build a deployment-ready end-to-end Machine Learning solution.
- 💻 Strengthen practical skills in Python, Data Analytics, Machine Learning, Regression Modeling, and Model Deployment through a real-world salary prediction use case.
  
---

# 📊 Dataset Information

### Dataset Name

Data Science Salaries Dataset

### Total Records

* 105,434 Records

### Total Features

* 11 Features

---

## Features Description

| Feature            | Description                               |
| ------------------ | ----------------------------------------- |
| work_year          | Year of Employment                        |
| experience_level   | Employee Experience Level                 |
| employment_type    | Full-time, Part-time, Contract, Freelance |
| job_title          | Employee Job Role                         |
| salary             | Original Salary                           |
| salary_currency    | Salary Currency                           |
| salary_in_usd      | Salary Converted to USD (Target Variable) |
| employee_residence | Employee Country                          |
| remote_ratio       | Remote Work Percentage                    |
| company_location   | Company Location                          |
| company_size       | Small, Medium, Large Company              |

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

# 📂 Project Structure

```bash
Salary_Prediction_Project/
│
├── app.py
├── model.pkl
├── salaries.csv
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── salary_prediction.ipynb
│
└── assets/
    └── screenshots/
```

---

# 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

### Salary Analysis

* Salary Distribution
* Salary by Experience Level
* Salary by Employment Type
* Salary by Company Size

### Location Analysis

* Salary by Employee Residence
* Salary by Company Location

### Job Analysis

* Salary by Job Title
* Salary by Work Year

### Correlation Analysis

* Correlation Heatmap
* Feature Importance Analysis

---

# ⚙️ Data Preprocessing

The following preprocessing techniques were applied:

### Missing Value Handling

* Checked Missing Values
* Removed Inconsistent Records

### Encoding

Categorical Features Converted Using:

* Label Encoding
* One-Hot Encoding

### Feature Scaling

Applied:

```python
StandardScaler()
```

for numerical features.

### Train-Test Split

```python
train_test_split()
```

used to split the dataset into training and testing sets.

---

# 🤖 Machine Learning Models Used

## 1. Linear Regression

Advantages:

* Simple and Interpretable
* Fast Training
* Strong Baseline Model

---

## 2. K-Nearest Neighbors (KNN)

Advantages:

* Easy to Implement
* Learns Patterns from Similar Data Points
* Effective for Regression Tasks

---

## 3. Decision Tree Regressor

Advantages:

* Handles Nonlinear Relationships
* Easy Visualization
* Feature Importance Analysis

---

## 4. Random Forest Regressor

Advantages:

* High Prediction Accuracy
* Reduces Overfitting
* Robust Performance

---

# 📈 Model Evaluation Metrics

The models were evaluated using:

### Mean Absolute Error (MAE)

Measures average prediction error.

### Mean Squared Error (MSE)

Measures squared prediction error.

### Root Mean Squared Error (RMSE)

Provides error in original units.

### R² Score

Measures how well the model explains variance.

---

# 🏆 Best Model Selection

Models were compared based on:

* R² Score
* MAE
* MSE
* RMSE
* Generalization Performance

Models Compared:

* Linear Regression
* K-Nearest Neighbors (KNN)
* Decision Tree Regressor
* Random Forest Regressor

The best-performing model was selected and saved for deployment.

---

# 💻 Streamlit Application

The application allows users to enter:

* Experience Level
* Employment Type
* Job Title
* Company Size
* Company Location
* Remote Ratio

### Output

* Predicted Salary in USD

The prediction is generated instantly using the trained Machine Learning model.

---

# ▶️ Run Locally

### Clone Repository

```bash
git clone https://github.com/yourusername/salary-prediction.git
```

### Navigate to Project Folder

```bash
cd salary-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
```

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Data Cleaning
* Feature Engineering
* Data Visualization
* Regression Models
* Model Evaluation
* Hyperparameter Tuning
* Streamlit Deployment
* End-to-End Machine Learning Workflow

---

# 🔮 Future Improvements

* Deep Learning Models
* Salary Trend Forecasting
* Real-Time Job Market Integration
* Interactive Analytics Dashboard
* AI Career Recommendation System

---

# 📜 Disclaimer

This project is developed for educational and research purposes only.

The predicted salaries are generated using machine learning models trained on historical salary data and should not be considered official compensation benchmarks or financial advice.

---

# ✅ Conclusion

This project demonstrates how Machine Learning can be used to predict employee salaries based on professional, organizational, and geographical factors. By comparing Linear Regression, K-Nearest Neighbors (KNN), Decision Tree, and Random Forest algorithms, the system provides accurate salary estimates and valuable insights into salary trends within the Data Science and AI industry.

---

# 👨‍💻 Author

**Rishu Gurjar**

Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer

### Skills

* Python
* SQL
* Machine Learning
* Data Analysis
* Streamlit
* Scikit-Learn
