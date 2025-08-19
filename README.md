📩 SMS Spam Classifier

This project is a Machine Learning-based web application that classifies SMS messages as either Spam or Ham (Not Spam).
It uses Natural Language Processing (NLP) techniques and a trained ML model to identify unwanted spam messages.

🚀 Features

Classifies text messages into Spam or Ham

Built using Machine Learning (NLP + Classification Algorithms)

Simple web interface with index.html and result.html

Real-time message classification

🛠️ Tech Stack

Python

Scikit-learn (Machine Learning)

NLTK (Text Preprocessing)

Flask (Web Framework)

HTML/CSS (Frontend)

📊 Dataset

The dataset used is the SMS Spam Collection Dataset.

Contains 5,574 labeled SMS messages tagged as ham or spam.

⚙️ Workflow

Data Preprocessing

Removed stopwords, punctuation, and applied tokenization.

Used TF-IDF Vectorization for feature extraction.

Model Training

Tried different classification algorithms (Naive Bayes, Logistic Regression, SVM, etc.).

Selected the best performing model.

Deployment

Built a Flask app with two HTML templates:

index.html → Input form for SMS text

result.html → Displays classification result

▶️ How to Run Locally

Clone the repository

https://github.com/Aanushkabhor/SMS_spam_detectio


Install dependencies

pip install -r requirements.txt


Run the Flask app

python app.py


Open in browser

http://127.0.0.1:5000/
