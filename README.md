# CoPlexi

A model for text classification

This project contains a text classification pipeline to automatically categorize financial transactions (e.g., deposits, withdrawals, purchases).
It uses **Python, scikit-learn, gensim, and Word2Vec** for preprocessing and model training.

---

### 🚀 Getting Started

#### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/coplexi.git
cd coplexi
```

#### 2. Create and activate a virtual environment

On Linux/Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### ⚡ Usage

#### Run pipeline

```bash
python src/pipeline.py
```

Expected output

```css
BKOFAMERICA MOBILE 04/05 3900761234 DEPOSIT  -->  deposit
Online Banking Transfer Conf# Ikaw7j6m0; LANNISTER, TYWIN  -->  purchase
Online Banking transfer from SAV 1234 Confirmation# 7341811234  -->  purchase
E-ZPASS REBILL DES:EZP REBILL ID:2018876 INDN:JON *SNOW CO  -->  purchase
CHECKCARD 0327 GOOGLE *Google Storage 855-836-3987 CA 24692164087108486320595  -->  purchase
...
KEEPTHECHANGE CREDIT FROM ACCT4567 EFFECTIVE 04/19  -->  deposit
KEEPTHECHANGE CREDIT FROM ACCT4567 EFFECTIVE 04/22  -->  deposit
Online Banking transfer to CHK 4567 Confirmation# 7341810000  -->  purchase
Monthly Maintenance Fee  -->  maintenance
```

---

### 📌 Requirements

- Python 3.9+
- pip
- virtualenv (recommended)
