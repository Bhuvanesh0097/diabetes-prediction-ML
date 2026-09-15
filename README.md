# Diabetes Prediction using Logistic Regression

A machine learning web application that predicts the likelihood of diabetes based on patient health and lifestyle information.

This project was developed as part of my journey in learning Machine Learning, starting with regression algorithms and progressing towards classification. After working with Linear Regression, I built this project to understand and implement Logistic Regression, model preprocessing, API development, and cloud deployment.

## Live Demo

**Live Application:**  
https://diabetes-prediction-ml-x41a.onrender.com/

The application allows users to enter patient information through a web interface and receive a prediction from the trained machine learning model.

---

## Project Overview

The objective of this project was to take a machine learning model beyond a notebook environment and deploy it as a usable web application.

The complete workflow is:

```text
Kaggle Dataset
      ↓
Data Preprocessing
      ↓
Feature Encoding & Scaling
      ↓
Logistic Regression
      ↓
Model Evaluation
      ↓
Model Serialization using Joblib
      ↓
Flask REST API
      ↓
GitHub
      ↓
Render Deployment
      ↓
Web Frontend
      ↓
User Prediction
Dataset

The dataset used in this project was obtained from Kaggle.

The dataset contains patient-related health and lifestyle features that can be used to predict whether a person is likely to have diabetes.

Features used
Feature	Description
gender	Gender of the patient
age	Age of the patient
hypertension	Whether the patient has hypertension
heart_disease	Whether the patient has heart disease
smoking_history	Patient's smoking history
bmi	Body Mass Index
HbA1c_level	HbA1c level
blood_glucose_level	Blood glucose level
Target

The target variable represents the diabetes outcome:

0 → Non-diabetic
1 → Diabetic
Machine Learning Approach

I used Logistic Regression for this project because the target is a binary classification problem.

The model was trained using Google Colab after preprocessing the dataset.

Preprocessing

The project uses a preprocessing pipeline containing:

StandardScaler for numerical features
OneHotEncoder for categorical features

The preprocessing and Logistic Regression model are combined into a single Scikit-learn Pipeline.

This ensures that the same preprocessing steps used during training are automatically applied when a user provides new data.

How user input is processed

For example, the user may enter:

Gender: Male
Smoking History: Never
Age: 45
BMI: 27.5
HbA1c: 6.2
Blood Glucose: 140

The input goes through the following process:

User Input
    ↓
Categorical Features
    ↓
OneHotEncoder
    ↓
Numerical Representation

Numerical Features
    ↓
StandardScaler
    ↓
Scaled Numerical Values

Both
    ↓
Logistic Regression
    ↓
Prediction + Probability

The Logistic Regression model receives numerical features after preprocessing and generates the final prediction.

Model Performance

The Logistic Regression model achieved an accuracy of:

96.05%

Note: The interpretation of this accuracy depends on how the evaluation dataset was created. Accuracy should be reported as test accuracy only when it is calculated on a held-out test set that was not used during model training.

Model Serialization

After training, the trained machine learning pipeline was saved using Joblib.

diabetes_logistic_regression_model.joblib

The saved pipeline contains the preprocessing steps and the Logistic Regression model.

This allows the deployed application to load the trained model directly without retraining it every time the server starts.

Flask API

The trained model was converted into a REST API using Flask.

Prediction Endpoint
POST /predict

The API accepts patient information in JSON format.

Example Request
{
  "gender": "Male",
  "age": 45,
  "hypertension": 0,
  "heart_disease": 0,
  "smoking_history": "never",
  "bmi": 27.5,
  "HbA1c_level": 6.2,
  "blood_glucose_level": 140
}
Example Response
{
  "status": "success",
  "prediction": 0,
  "diabetes_probability": 0.1234,
  "message": "Non-diabetic"
}

The response contains both the predicted class and the model's estimated probability.

Frontend

A simple frontend was developed using:

HTML
CSS
JavaScript

The frontend provides input fields for the required patient information.

When the user clicks Predict Diabetes Risk, JavaScript sends the input data to the Flask /predict endpoint.

The prediction returned by the API is then displayed directly in the user interface.

The frontend is intentionally kept simple because the primary focus of this project was understanding the Machine Learning workflow and deployment process.

Deployment

The application was deployed using Render.

Technologies used for deployment
GitHub → Source Code & Model Storage
Render  → Cloud Deployment
Flask   → Backend API

The deployed application can be accessed here:

https://diabetes-prediction-ml-x41a.onrender.com/

Project Structure
diabetes-prediction-ML/
│
├── app.py
│
├── diabetes_logistic_regression_model.joblib
│
├── scaler.joblib
│
├── requirements.txt
│
├── README.md
│
└── templates/
    └── index.html
File Description
File	Purpose
app.py	Flask backend and prediction API
diabetes_logistic_regression_model.joblib	Trained ML pipeline
scaler.joblib	Saved scaler used during experimentation
requirements.txt	Python dependencies
templates/index.html	Frontend interface
README.md	Project documentation
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Logistic Regression
StandardScaler
OneHotEncoder
Joblib
Flask
HTML
CSS
JavaScript
Google Colab
Kaggle
GitHub
Render
What I Learned

This project helped me understand the complete journey of a machine learning model:

Finding and understanding a dataset
Data preprocessing
Handling categorical and numerical features
Training a classification model
Evaluating model performance
Saving a trained model
Building a REST API using Flask
Connecting a frontend to an ML API
Deploying a machine learning application to the cloud
Understanding the difference between a local ML notebook and a deployable ML application

One of the most important things I learned is that building an ML project does not end with achieving good accuracy. Making the trained model accessible through an API and usable through a frontend is an important part of taking ML towards a real application.

Linear Regression vs Logistic Regression

This project was my next step after learning Linear Regression.

Linear Regression

Used mainly for predicting continuous numerical values.

Input → Linear Regression → Continuous Value

Example:

House Features → Predicted House Price
Logistic Regression

Used mainly for classification problems.

Input → Logistic Regression → Probability → Class

Example:

Patient Information
        ↓
Logistic Regression
        ↓
Diabetes Probability
        ↓
Diabetic / Non-diabetic
Future Improvements

This project is an early step in my Machine Learning journey, and there are several areas I would like to explore next:

Experiment with XGBoost
Compare multiple classification algorithms
Perform more detailed model evaluation
Explore feature importance and model interpretability
Improve frontend design and user experience
Add better input validation
Explore more advanced deployment practices
Work with larger and more diverse datasets

My next major learning goal is to explore XGBoost and understand how more powerful tree-based models compare with Logistic Regression.

Disclaimer

This application is an educational machine learning project.

The prediction generated by this application is not a medical diagnosis and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

Author

Bhuvanesh

Machine Learning Learner | Python 

This project represents one step in my journey from learning individual ML algorithms to building and deploying complete machine learning applications.
