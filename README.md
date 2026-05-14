# 📰 Fake News Detection App

A Machine Learning and NLP-based web application that detects whether a news article is **Fake** or **Real**.

---

# 📌 Project Overview

This project uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to classify news articles as fake or real.

The application takes news text as input, preprocesses it using NLP techniques, converts the text into numerical vectors using **TF-IDF Vectorization**, and predicts the result using a trained **Logistic Regression** model.

The project is deployed using **Streamlit** for real-time user interaction.

---

# 🚀 Features

- Detects Fake and Real News
- NLP-based text preprocessing
- TF-IDF vectorization
- Logistic Regression classification
- User-friendly Streamlit interface
- Real-time prediction

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Streamlit
- Pickle

---

# 📂 Dataset Information

Dataset used:

Fake and Real News Dataset from Kaggle

🔗 Dataset Link:  
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

---

# 📊 Dataset Description

The dataset contains approximately 45,000 news articles categorized as fake or real news.

The dataset consists of two CSV files:

- `Fake.csv` → Contains fake news articles
- `True.csv` → Contains real news articles

---

# 📁 Dataset Columns

| Column Name | Description |
|-------------|-------------|
| title | News headline |
| text | Full news article |
| subject | News category |
| date | Publication date |

---

# 🧹 Data Preprocessing Steps

The following preprocessing techniques were applied:

- Converted text to lowercase
- Removed URLs
- Removed special characters
- Removed numbers
- Removed extra spaces
- Removed duplicate records

---

# 🔍 NLP Techniques Used

- Text Cleaning
- Tokenization
- TF-IDF Vectorization
- Text Classification

---

# 🤖 Machine Learning Model

Algorithm used:

- Logistic Regression

The model was trained using TF-IDF feature vectors generated from the news article text.

---

# 📈 Model Workflow

News Text  
↓  
Text Cleaning  
↓  
TF-IDF Vectorization  
↓  
Logistic Regression Model  
↓  
Prediction (Fake / Real)

---

# 📦 Project Structure

```bash
fake-news-detector/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── fake_news_model.ipynb
```
