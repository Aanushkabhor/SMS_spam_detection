from flask import Flask, render_template, request
import pickle
import re
import string

# ✅ Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

def clean_text(text):
    # Example: Lowercase, remove punctuation, etc.
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    return text

@app.route('/')
def home():
    return render_template('index.html')   # show form page

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        cleaned_message = clean_text(message)
        data = [cleaned_message]
        vect = tfidf.transform(data)
        prediction = model.predict(vect)[0]
        label = "spam" if prediction == 1 else "ham"  # Convert 1/0 to label

        return render_template('result.html', 
                               message=message,
                               prediction=label)                           

if __name__ == '__main__':
    app.run(debug=True)
