import json

from models.train import train_model
from models.predict import predict_transactions, exported_predict_transactions

if __name__ == "__main__":
    with open("src/data/dataset_2.json", "r") as f:
        data = json.load(f)

    transactions = data["Account"]["Transactions"]["Transaction"]

    w2v_model, clf = train_model(transactions)

    predict_transactions(transactions, w2v_model, clf, limit=100)
    exported_predict_transactions(transactions, w2v_model, clf, limit=100)
