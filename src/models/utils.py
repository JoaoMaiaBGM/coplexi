import numpy as np
import pickle
import os
from pathlib import Path
from gensim.models import Word2Vec

def preprocess_text(text: str):
    return [word.lower() if not word.isdigit() else "NUM" for word in text.split()]

def vectorize(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

def save_model(w2v_model, clf, model_dir="models_data"):
    os.makedirs(model_dir, exist_ok=True)

    w2v_path = os.path.join(model_dir, "w2v_model.model")
    w2v_model.save(w2v_path)

    clf_path = os.path.join(model_dir, "classifier.pkl")
    with open(clf_path, "wb") as f:
        pickle.dump(clf, f)

    print(f"Models saved to {model_dir}/")

def load_model(model_dir="models_data"):

    w2v_path = os.path.join(model_dir, "w2v_model.model")
    clf_path = os.path.join(model_dir, "classifier.pkl")

    if not os.path.exists(w2v_path) or not os.path.exists(clf_path):
        raise FileNotFoundError(
            f"Models not found in {model_dir}/. Please train the model first."
        )

    w2v_model = Word2Vec.load(w2v_path)

    with open(clf_path, "rb") as f:
        clf = pickle.load(f)

    print(f"Models loaded from {model_dir}/")
    return w2v_model, clf
