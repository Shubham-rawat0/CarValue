# CarValue – Car Price Prediction Platform

CarValue is a modern machine learning web application that predicts the resale value of a car based on its specifications.  
It combines a trained ML model with a scalable API backend and an interactive frontend to deliver fast and accurate price predictions.

The system is designed with a clean architecture using a **FastAPI backend deployed on Render** and a **Streamlit frontend deployed on Streamlit Cloud**, making it suitable for real-world ML deployment scenarios.

---

## Features

###  Car Price Prediction
- Predict the resale value of a car instantly
- Uses a trained **Random Forest Regression model**
- Accepts car attributes such as year, fuel type, transmission, etc.

###  Machine Learning Model
- Trained using **scikit-learn**
- Feature preprocessing using pandas
- Model serialized using Joblib for fast inference

###  Modern Web Interface
- Interactive UI built with Streamlit
- Clean dashboard-style layout
- Instant prediction results

###  Fast API Backend
- High-performance API using FastAPI
- REST endpoint for ML inference
- Designed for scalable deployments


## Tech Stack

### Frontend
- Streamlit
- Python
- Requests

### Backend
- FastAPI
- Uvicorn
- Pydantic

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib


## Project Architecture

```
User Browser
      │
      ▼
Streamlit Frontend (UI)
      │
HTTP Request
      │
      ▼
FastAPI Backend (Render)
      │
      ▼
Machine Learning Model (.pkl)
      │
      ▼
Predicted Car Price
```

---

## How It Works

### 1️⃣ User Input
The user enters car details such as:
- Car Name
- Manufacturing Year
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Owner Type

---

### 2️⃣ API Request
The Streamlit frontend sends a request to the FastAPI backend:

```
POST /predict
```

The request contains the car features in JSON format.

---

### 3️⃣ Data Preprocessing
The backend:
- Converts input data into a dataframe
- Applies feature encoding (One-Hot Encoding)
- Aligns input features with the trained model columns

---

### 4️⃣ Model Prediction
The trained **Random Forest model** predicts the car price.

---

### 5️⃣ Result Display
The predicted resale value is returned to the frontend and displayed to the user instantly.

---

## Run Locally

### Prerequisites

- Python 3.10+
- Git

---

### Clone the Repository

```bash
git clone https://github.com/Shubham-rawat0/carvalue.git
cd carvalue
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the FastAPI Backend

```bash
uvicorn main:app --reload
```

API will run on:

```
http://127.0.0.1:8000
```

---

### Run the Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

The UI will open in your browser.

---

