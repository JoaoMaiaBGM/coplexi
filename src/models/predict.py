import pandas as pd
from tabulate import tabulate
from .utils import preprocess_text, vectorize
import dataframe_image as dfi

def predict_transactions(transactions, w2v_model, clf, limit=100):
    results = []

    for text in transactions[:limit]:
        tokens = preprocess_text(text["narration"])
        vec = vectorize(tokens, w2v_model).reshape(1, -1)
        pred = clf.predict(vec)[0]
        results.append({
            "Narration": text["narration"],
            "Prediction": pred
        })

    df = pd.DataFrame(results)

    output = tabulate(df, headers=["Na", "Prediction"], tablefmt="simple_grid", showindex="always")
    print(output)

    return df

def exported_predict_transactions(transactions, w2v_model, clf, limit=100, export="predictions.csv"):
    results_to_export = []

    for text in transactions[:limit]:
        tokens = preprocess_text(text["narration"])
        vec = vectorize(tokens, w2v_model).reshape(1, -1)
        pred = clf.predict(vec)[0]
        results_to_export.append({
            "Na": text["narration"],
            "Prediction": pred
        })

    df = pd.DataFrame(results_to_export)
    df.to_csv(export, index=True)