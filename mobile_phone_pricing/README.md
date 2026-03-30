# 📱 Mobile Phone Price Prediction using Machine Learning

## 📌 Project Overview
This project aims to build a **machine learning classification system** that predicts the **price range of mobile phones**
based on their technical specifications.

The model classifies mobile phones into four categories:
- **Low Cost**
- **Medium Cost**
- **High Cost**
- **Very High Cost**

This project demonstrates the complete **machine learning workflow** including data exploration, preprocessing,
model training, evaluation, and prediction.

---

## 🎯 Objective
To predict the **price category of a mobile phone** using features such as:
- Battery capacity
- RAM
- Camera quality
- Screen resolution
- Connectivity options
- Hardware specifications

---

## 🧠 Problem Type
- **Supervised Learning**
- **Multiclass Classification**

---

## 📊 Dataset Description
The dataset contains specifications of mobile phones available in the market.

### 🔹 Features
- `battery_power` – Battery capacity (mAh)
- `blue` – Bluetooth support (0/1)
- `clock_speed` – Processor speed
- `dual_sim` – Dual SIM support
- `fc` – Front camera megapixels
- `four_g` – 4G support
- `int_memory` – Internal memory (GB)
- `m_dep` – Mobile depth (cm)
- `mobile_wt` – Weight (grams)
- `n_cores` – Number of CPU cores
- `pc` – Primary camera megapixels
- `px_height` – Pixel resolution height
- `px_width` – Pixel resolution width
- `ram` – RAM (MB)
- `sc_h` – Screen height (cm)
- `sc_w` – Screen width (cm)
- `talk_time` – Battery talk time (hours)
- `three_g` – 3G support
- `touch_screen` – Touch screen support
- `wifi` – WiFi support

### 🎯 Target Variable
- `price_range`
  - `0` → Low Cost
  - `1` → Medium Cost
  - `2` → High Cost
  - `3` → Very High Cost

---

## 🛠️ Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 🤖 Machine Learning Models Implemented
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

---

## 🏆 Best Performing Model
**Random Forest Classifier** achieved the highest accuracy and was selected as the final model
for prediction and evaluation.

---

## 📁 Project Structure

Mobile_Phone_Price_Prediction/
│
├── Mobile_Phone_Price_Prediction.ipynb
├── dataset.csv
├── requirements.txt
└── README.md



---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Mobile_Phone_Price_Prediction.git
cd Mobile_Phone_Price_Prediction

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Notebook
jupyter notebook mobile_phone_pricing.ipynb



---

Nikhil Anand
Machine Learning Project
