from .utils import preprocess_text, vectorize

def predict_transactions(transactions, w2v_model, clf, limit=20):
    for text in transactions[:limit]:
        tokens = preprocess_text(text["description"])
        vec = vectorize(tokens, w2v_model).reshape(1, -1)
        pred = clf.predict(vec)[0]
        print(f"{text['description']}  -->  {pred}")
