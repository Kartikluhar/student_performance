# 🎓 Student Performance Analysis & Prediction System

A **Django-based Machine Learning web application** that analyzes student academic performance and predicts final grades using the **UCI Student Performance Dataset**. The application provides an interactive analytics dashboard, visualizes student insights, and allows users to upload their own CSV datasets for analysis.

---

## 📌 Overview

This project combines **Machine Learning**, **Data Analysis**, and **Web Development** to help analyze student performance based on academic and behavioral factors.

The system predicts a student's **final grade (G3)** using a trained regression model and presents meaningful insights through interactive charts and dashboards.

---

## ✨ Features

- 📁 Upload CSV datasets for analysis
- 🤖 Predict student final grades using a trained Machine Learning model
- 📊 Interactive dashboard with performance analytics
- 📈 Visualize trends using Charts.js
- 📉 Analyze student performance distributions
- 📋 Display processed dataset in tabular format
- 📱 Fully responsive user interface
- ⚡ Fast and user-friendly experience

---

## 🧠 Machine Learning Model

### Target Variable
- **G3 (Final Grade)**

### Features Used
- G1 (First Period Grade)
- G2 (Second Period Grade)
- Failures
- Study Time
- Absences

### Model Performance

| Metric | Value |
|---------|-------|
| R² Score | **87%** |

The model was trained using supervised machine learning techniques to accurately predict students' final grades based on historical academic data.

---

## 📊 Dashboard Features

The dashboard provides:

- Student performance overview
- Grade distribution analysis
- Performance trends
- Interactive charts
- Dataset summary
- Prediction results
- Data visualization

---

## 🛠️ Tech Stack

### Backend
- Django
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Frontend
- HTML5
- CSS3
- Bootstrap
- JavaScript
- Charts.js

### Dataset
- UCI Student Performance Dataset

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kartikluhar/student_performance.git
```

### 2. Navigate to the Project

```bash
cd student-performance-analysis
```

### 3. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📈 Workflow

```text
CSV Dataset
      │
      ▼
Upload Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Machine Learning Prediction
      │
      ▼
Analytics Dashboard
      │
      ▼
Performance Visualization
```

---

## 📷 Screenshots

> Add screenshots of your project here.

### Dashboard

```
screenshots/dashboard.png
```

### Prediction Page

```
screenshots/prediction.png
```

### Analytics

```
screenshots/analytics.png
```

---

## 📚 Learning Outcomes

This project helped strengthen my knowledge in:

- Machine Learning Model Development
- Regression Algorithms
- Data Cleaning & Preprocessing
- Data Visualization
- Django Web Development
- Dashboard Design
- CSV File Processing
- Backend Development
- Responsive UI Design

---

## 🚀 Future Improvements

- Authentication & User Accounts
- Multiple Machine Learning Algorithms
- Download Prediction Reports
- PDF Report Generation
- Advanced Student Analytics
- Model Comparison Dashboard
- Performance History Tracking
- Cloud Deployment

---

## 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Kartik Luhar**

- Python Developer
- Django Developer
- Machine Learning Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub.
```
