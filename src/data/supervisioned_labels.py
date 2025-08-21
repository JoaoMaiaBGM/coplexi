import pandas as pd

from models.utils import preprocess_text

def load_labels():
    labels = [
    ("BKOFAMERICA MOBILE 04/05 3900761234 DEPOSIT", "deposit"),
    ("Monthly Maintenance Fee", "maintenance"),
    ("PAYMENT AMAZON 04/07", "payment"),
    ("TRANSFER TO SAVINGS 04/08", "transfer"),
    ("E-ZPASS REBILL DES:EZP REBILL ID:2018876 INDN:JON *SNOW CO", "purchase"),
    ("CHECKCARD 0327 GOOGLE *Google Storage 855-836-3987 CA 24692164087108486320595", "purchase"),
    ################################################################################################
    ("BKOFAMERICA MOBILE 04/05 3900761234 DEPOSIT", "deposit"),
    ("Monthly Maintenance Fee", "maintenance"),
    ("PAYMENT AMAZON 04/07", "payment"),
    ("TRANSFER TO SAVINGS 04/08", "transfer"),
    ("E-ZPASS REBILL DES:EZP REBILL ID:2018876 INDN:JON *SNOW CO", "purchase"),
    ("CHECKCARD 0327 GOOGLE *Google Storage 855-836-3987 CA 24692164087108486320595", "purchase"),
]

    df_labels = pd.DataFrame(labels, columns=["description", "category"])
    df_labels["tokens"] = df_labels["description"].apply(preprocess_text)
    return df_labels