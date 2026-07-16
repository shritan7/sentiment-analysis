from flask import Flask, render_template, request
import joblib

from preprocess import preprocess

app = Flask(__name__)

model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    review = request.form["review"]

    clean_review = preprocess(review)

    review_vector = vectorizer.transform([clean_review])

    prediction = model.predict(review_vector)

    probabilities = model.predict_proba(review_vector)

    confidence = max(probabilities[0]) * 100

    result = prediction[0]

    return render_template(
        "index.html",
        prediction=result,
        confidence=round(confidence, 2)
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)