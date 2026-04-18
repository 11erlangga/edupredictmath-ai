# edupredictmath-ai

> 🇮🇩 Bahasa Indonesia | 🇬🇧 [English](#english-version)

---

## 🇮🇩 Versi Bahasa Indonesia

Repositori ini berisi **AI Service** dari project EduPredictMath — bagian yang bertanggung jawab atas prediksi penguasaan konsep matematika siswa menggunakan model Knowledge Tracing.

### 📁 Struktur Repositori

```
edupredictmath-ai/
├── ai-service/                        # API yang di-deploy ke Railway
│   ├── main.py                        # Entry point FastAPI
│   ├── requirements.txt               # Dependencies Python
│   ├── routers/
│   │   └── predict.py                 # POST /predict endpoint
│   ├── schemas/
│   │   └── predict.py                 # Pydantic input/output schemas
│   ├── services/
│   │   └── inference.py               # Business logic prediksi
│   ├── models/
│   │   ├── base_model.py              # Abstract base class semua model
│   │   ├── dkt_model.py               # Model loader & inference operasional
│   │   └── architectures/             # Definisi arsitektur model
│   │       ├── __init__.py
│   │       ├── dkt_plus.py            # DKT+
│   │       ├── sakt.py                # SAKT
│   │       ├── simple_kt.py           # simpleKT
│   │       └── saint.py               # SAINT
│   └── saved_model/                   # Hasil training (tidak masuk Git)
│
├── notebooks/                         # Eksperimen & training (tidak di-deploy)
│   ├── 01_eda.ipynb                   # Eksplorasi data
│   ├── 02_preprocessing.ipynb         # Preprocessing data
│   ├── 03_dkt_plus.ipynb              # Training DKT+
│   ├── 04_sakt.ipynb                  # Training SAKT
│   ├── 05_simple_kt.ipynb             # Training simpleKT
│   ├── 06_saint.ipynb                 # Training SAINT
│   └── dummy_data.py                  # Script generate dummy data
│
├── data/
│   ├── raw/                           # Data mentah (tidak masuk Git)
│   └── processed/                     # Data hasil preprocessing (tidak masuk Git)
│
├── .gitignore
└── README.md
```

> ⚠️ Folder `saved_model/`, `data/raw/`, dan `data/processed/` tidak masuk Git karena ukurannya besar. File-file tersebut disimpan di Google Drive tim.

---

### ⚙️ Setup & Cara Menjalankan

#### Prasyarat
- Python 3.10+
- Conda (direkomendasikan)

#### 1. Clone repositori
```bash
git clone https://github.com/11erlangga/edupredictmath-ai.git
cd edupredictmath-ai
```

#### 2. Buat dan aktifkan environment Conda
```bash
conda create -n edupredictmath python=3.10
conda activate edupredictmath
```

#### 3. Install dependencies
```bash
cd ai-service
pip install -r requirements.txt
```

#### 4. Jalankan API
```bash
uvicorn main:app --reload
```

API akan berjalan di `http://localhost:8000`.
Dokumentasi otomatis tersedia di `http://localhost:8000/docs`.

---

### 🔗 Endpoint

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Health check |
| POST | `/predict` | Prediksi penguasaan konsep siswa |

#### Contoh Request `/predict`
```json
{
  "user_id": "student_001",
  "preferences": {
    "interest": "algebra"
  },
  "history": [
    { "concept_id": 1, "correctness": 1 },
    { "concept_id": 2, "correctness": 0 }
  ],
  "query_concept": 3
}
```

---

### 🤝 Cara Kontribusi

1. Pastikan kamu sudah di-invite sebagai **Collaborator** di repo ini
2. Jangan langsung push ke branch `main`
3. Buat branch baru untuk setiap fitur atau perbaikan:
```bash
git checkout -b feat/nama-fitur
```
4. Setelah selesai, buat **Pull Request** ke branch `main`
5. Minta review ke AI Engineer sebelum merge

---

### 📌 Catatan Penting

- File `.env` **jangan pernah di-push** ke GitHub. Simpan API key dan secret di file `.env` lokal atau di Railway Environment Variables
- Hasil training model disimpan di **Google Drive tim**, bukan di repo ini
- Notebook training dijalankan di **Google Colab**

---
---

## English Version

This repository contains the **AI Service** of the EduPredictMath project — the component responsible for predicting students' math concept mastery using Knowledge Tracing models.

### 📁 Repository Structure

```
edupredictmath-ai/
├── ai-service/                        # API deployed to Railway
│   ├── main.py                        # FastAPI entry point
│   ├── requirements.txt               # Python dependencies
│   ├── routers/
│   │   └── predict.py                 # POST /predict endpoint
│   ├── schemas/
│   │   └── predict.py                 # Pydantic input/output schemas
│   ├── services/
│   │   └── inference.py               # Prediction business logic
│   ├── models/
│   │   ├── base_model.py              # Abstract base class for all models
│   │   ├── dkt_model.py               # Model loader & operational inference
│   │   └── architectures/             # Model architecture definitions
│   │       ├── __init__.py
│   │       ├── dkt_plus.py            # DKT+
│   │       ├── sakt.py                # SAKT
│   │       ├── simple_kt.py           # simpleKT
│   │       └── saint.py               # SAINT
│   └── saved_model/                   # Trained model artifacts (not in Git)
│
├── notebooks/                         # Experiments & training (not deployed)
│   ├── 01_eda.ipynb                   # Exploratory data analysis
│   ├── 02_preprocessing.ipynb         # Data preprocessing
│   ├── 03_dkt_plus.ipynb              # DKT+ training
│   ├── 04_sakt.ipynb                  # SAKT training
│   ├── 05_simple_kt.ipynb             # simpleKT training
│   ├── 06_saint.ipynb                 # SAINT training
│   └── dummy_data.py                  # Dummy data generation script
│
├── data/
│   ├── raw/                           # Raw data (not in Git)
│   └── processed/                     # Preprocessed data (not in Git)
│
├── .gitignore
└── README.md
```

> ⚠️ The `saved_model/`, `data/raw/`, and `data/processed/` folders are excluded from Git due to large file sizes. These are stored in the team's Google Drive.

---

### ⚙️ Setup & How to Run

#### Prerequisites
- Python 3.10+
- Conda (recommended)

#### 1. Clone the repository
```bash
git clone https://github.com/11erlangga/edupredictmath-ai.git
cd edupredictmath-ai
```

#### 2. Create and activate Conda environment
```bash
conda create -n edupredictmath python=3.10
conda activate edupredictmath
```

#### 3. Install dependencies
```bash
cd ai-service
pip install -r requirements.txt
```

#### 4. Run the API
```bash
uvicorn main:app --reload
```

The API will run at `http://localhost:8000`.
Auto-generated documentation is available at `http://localhost:8000/docs`.

---

### 🔗 Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/predict` | Predict student concept mastery |

#### Example `/predict` Request
```json
{
  "user_id": "student_001",
  "preferences": {
    "interest": "algebra"
  },
  "history": [
    { "concept_id": 1, "correctness": 1 },
    { "concept_id": 2, "correctness": 0 }
  ],
  "query_concept": 3
}
```

---

### 🤝 How to Contribute

1. Make sure you have been invited as a **Collaborator** on this repo
2. Never push directly to the `main` branch
3. Create a new branch for each feature or fix:
```bash
git checkout -b feat/feature-name
```
4. When done, open a **Pull Request** to the `main` branch
5. Request a review from the AI Engineer before merging

---

### 📌 Important Notes

- **Never push** the `.env` file to GitHub. Store API keys and secrets in your local `.env` file or in Railway Environment Variables
- Trained model artifacts are stored in the **team's Google Drive**, not in this repository
- Training notebooks are run on **Google Colab**
