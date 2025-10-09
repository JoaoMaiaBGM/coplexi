import modal
from typing import Dict, List, Optional

app = modal.App(name="coplexi")

image = (
    modal.Image.debian_slim()
    .pip_install_from_requirements("requirements.txt")
    .add_local_dir("src", remote_path="/root/src")
    .add_local_dir("models_data", remote_path="/root/models_data")
)

volume = modal.Volume.from_name("coplexi-models", create_if_missing=True)

@app.function(
    image=image,
    volumes={"/models": volume}
)

def predict_transactions(transactions: List[Dict[str, str]]) -> List[Dict[str, str]]:

    import sys
    sys.path.insert(0, "/root")

    from src.models.utils import load_model, preprocess_text, vectorize

    w2v_model, clf = load_model("/root/models_data")

    results = []
    for transaction in transactions:
        description = transaction.get("description", "")

        tokens = preprocess_text(description)
        vec = vectorize(tokens, w2v_model).reshape(1, -1)

        prediction = clf.predict(vec)[0]

        results.append({
            "description": description,
            "prediction": prediction
        })

    return results

@app.local_entrypoint()
def main():
    test_transactions = [
        {"description": "Deposit"},
        {"description": "Purchase"},
        {"description": "Transfer"}
    ]

    result = predict_transactions.remote(test_transactions)
    print("\nResultados:")
    for item in result:
        print(f"{item['description']}: {item['prediction']}")

    return result
