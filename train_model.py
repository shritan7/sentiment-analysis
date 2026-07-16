import pandas as pd

from preprocess import preprocess

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score

import joblib

data = pd.read_csv("dataset/IMDB Dataset.csv")

data["review"] = data["review"].apply(preprocess)

X = data["review"]

y = data["sentiment"]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

joblib.dump(model, "model/sentiment_model.pkl")

joblib.dump(vectorizer, "model/vectorizer.pkl")