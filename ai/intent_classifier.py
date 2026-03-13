import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intent dataset
with open("data/intents.json") as f:
    intents = json.load(f)

texts = []
labels = []

for intent, examples in intents.items():
    for example in examples:
        texts.append(example)
        labels.append(intent)

# Convert text → vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

def predict_intent(message):

    vector = vectorizer.transform([message])

    prediction = model.predict(vector)[0]

    return prediction