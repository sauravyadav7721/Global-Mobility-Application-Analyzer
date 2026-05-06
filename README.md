# 🌍 Global Mobility Application Analyzer

An end-to-end **Machine Learning Pipeline Project** that predicts whether a visa application will be **Approved or Denied** using historical immigration data.

---

## 🚀 Project Overview

This project implements a **production-grade ML system** that automates:

* Data ingestion from MongoDB
* Data validation & preprocessing
* Feature engineering & transformation
* Model training & hyperparameter tuning
* Model evaluation & versioning
* Deployment using AWS & CI/CD pipelines

---

## 🎯 Problem Statement

Visa approval decisions depend on multiple factors such as:

* Education level
* Work experience
* Employer details
* Salary (prevailing wage)
* Region of employment

👉 This system helps:

* Predict approval chances
* Identify key influencing factors
* Automate decision support

---

## 🧠 Project Architecture

```
1. constants
2. config_entity
3. artifact_entity
4. components
5. pipeline
6. demo.py / app.py
```

---

## 🔄 ML Pipeline Workflow

### 1. Data Ingestion

* Fetch data from MongoDB
* Store in feature store

### 2. Data Validation

* Schema validation
* Data consistency checks

### 3. Data Transformation

* Encoding (OneHot + Ordinal)
* Feature scaling (StandardScaler)
* Power transformation (Yeo-Johnson)

### 4. Model Training

* Models used:

  * KNN
  * Random Forest
  * XGBoost
* Hyperparameter tuning:

  * RandomizedSearchCV

### 5. Model Evaluation

* Compare with previous model (stored in AWS S3)
* Select best-performing model

### 6. Deployment

* Store model in AWS S3
* CI/CD pipeline using GitHub Actions
* Dockerized deployment on EC2

---

## ⚙️ Tech Stack

* **Programming:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost
* **Database:** MongoDB
* **Cloud:** AWS S3, EC2
* **CI/CD:** GitHub Actions
* **Containerization:** Docker

---

## 📊 Dataset

Dataset used:
👉 https://www.kaggle.com/datasets/moro23/easyvisa-dataset

---

## ▶️ How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/sauravyadav7721/Global-Mobility-Application-Analyzer.git
cd Global-Mobility-Application-Analyzer
```

---

### 2. Create Virtual Environment

```bash
conda create -n application python=3.8 -y
conda activate application
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set Environment Variables

#### Windows:

```bash
set MONGODB_URL=your_mongodb_connection_string
set AWS_ACCESS_KEY_ID=your_access_key
set AWS_SECRET_ACCESS_KEY=your_secret_key
```

#### Linux / Mac:

```bash
export MONGODB_URL="your_mongodb_connection_string"
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
```

---

### 5. Run the Application

```bash
python demo.py
```

---

## ☁️ AWS CI/CD Deployment

### Steps:

1. Create IAM user with:

   * AmazonEC2FullAccess
   * AmazonEC2ContainerRegistryFullAccess

2. Create ECR repository

3. Launch EC2 instance (Ubuntu)

4. Install Docker:

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

5. Configure GitHub Actions Runner

6. Add GitHub Secrets:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_DEFAULT_REGION
* ECR_REPO
* MONGODB_URL

---

## 📈 Model Performance

* Cross-validation used for evaluation
* Multiple models compared
* Best model selected based on performance metrics

### Metrics Used:

* Accuracy
* Precision
* Recall
* F1 Score

---

## ⚠️ Challenges Faced

* Building modular ML pipeline
* Debugging configuration & artifacts
* Handling feature transformations
* AWS environment integration
* CI/CD setup

---

## 💡 Key Learnings

* End-to-end ML pipeline development
* Industry-level project structuring
* Debugging real-world ML systems
* Cloud deployment (AWS)
* CI/CD automation

---

## 🔮 Future Improvements

* Add FastAPI for real-time predictions
* Add Streamlit dashboard
* Implement SHAP for explainability
* Add model monitoring & drift detection

---

## 👨‍💻 Author

**Saurav Yadav**
Data Science Student | Machine Learning Enthusiast

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

