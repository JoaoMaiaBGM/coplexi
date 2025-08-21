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

#### Train the model

```bash
python src/train.py
```

This will preprocess the data, train the classifier, and save the model under src/models/.

#### Run predictions

```bash
python src/predict.py "ATM WITHDRAWAL 04/06 12345678"
```

Expected output

```css
Predicted label: withdrawal
```

---

### 🧪 Running Tests

```bash
pytest tests/
```

---

### 📌 Requirements

- Python 3.9+
- pip
- virtualenv (recommended)
