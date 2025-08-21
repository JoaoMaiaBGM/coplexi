import pandas as pd
from gensim.models import Word2Vec
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from .utils import preprocess_text, vectorize
from .data.supervisioned_labels import load_labels

def train_model(transactions):
    df_labels = load_labels()

    all_tokens = [preprocess_text(text["description"]) for text in transactions]
    label_tokens = df_labels["tokens"].tolist()
    corpus = all_tokens + label_tokens

    w2v_model = Word2Vec(
        sentences=corpus,
        vector_size=100,
        window=5,
        min_count=1
    )

    X = [vectorize(tokens, w2v_model) for tokens in df_labels["tokens"]]
    y = df_labels["category"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42, stratify=y
    )

    clf = LogisticRegression(
        class_weight="balanced",
        max_iter=1000
    )

    clf.fit(X_train, y_train)

    print("Classification report (labels):")
    print(classification_report(y_test, clf.predict(X_test)))

    return w2v_model, clf
