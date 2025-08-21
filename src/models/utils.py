import numpy as np

def preprocess_text(text: str):
    return [word.lower() if not word.isdigit() else "NUM" for word in text.split()]

def vectorize(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)
