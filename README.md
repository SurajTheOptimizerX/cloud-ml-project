# ☁️ Cloud-Deployed Machine Learning & Data Pipeline

## 📌 Project Overview

This project is an end-to-end Machine Learning pipeline that predicts student performance based on multiple factors such as study hours, attendance, and subject scores.

The model is built using Python and deployed using a Flask API, making it accessible for real-time predictions.

---

## 🚀 Features

* Data preprocessing using **Pandas**
* Handling categorical data with **One-Hot Encoding**
* Model training using **Random Forest Regressor**
* Model evaluation using **Mean Squared Error (MSE)**
* REST API built with **Flask**
* Ready for **Azure Cloud Deployment**

---

## 📂 Project Structure

```
cloud-ml-project/
│
├── app.py                  # Flask API
├── train.py                # Model training script
├── test_api.py             # API testing script
├── Student_Performance.csv # Dataset
├── model.pkl               # Trained model (generated)
├── README.md               # Project documentation
```

---

## 🧠 Machine Learning Pipeline

1. Data Collection (CSV dataset)
2. Data Cleaning & Preprocessing
3. Feature Encoding (categorical → numeric)
4. Model Training (Random Forest)
5. Model Evaluation (MSE)
6. Model Saving (joblib)
7. API Deployment (Flask)

---

## 📊 Sample Input (API)

```json
{
  "age": 16,
  "gender": "male",
  "school_type": "public",
  "parent_education": "graduate",
  "study_hours": 5,
  "attendance_percentage": 80,
  "internet_access": "yes",
  "travel_time": "<15 min",
  "extra_activities": "yes",
  "study_method": "notes",
  "math_score": 60,
  "science_score": 65,
  "english_score": 70
}
```

---

## 📈 Sample Output

```json
{
  "predicted_score": 73.5
}
```

---

## ⚙️ How to Run Locally

### 1. Clone Repository

```
git clone https://github.com/YOUR-USERNAME/cloud-ml-project.git
cd cloud-ml-project
```

### 2. Install Dependencies

```
pip install pandas scikit-learn flask joblib requests
```

### 3. Train Model

```
python train.py
```

### 4. Run API

```
python app.py
```

### 5. Test API

```
python test_api.py
```

---

## ☁️ Deployment

The project can be deployed on **Microsoft Azure Virtual Machine** to make the API publicly accessible.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Flask
* Joblib
* Microsoft Azure

---

## 🎯 Future Improvements

* Deploy using **Gunicorn (production server)**
* Add frontend UI
* Integrate Azure Blob Storage
* Improve model accuracy

---

## 👨‍💻 Author

Suraj Sahu
