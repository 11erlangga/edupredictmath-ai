ai-service/
├── main.py                  # Entry point FastAPI
├── routers/
│   └── predict.py           # POST /predict endpoint
├── models/
│   └── dkt_model.py         # Model loading & inference logic
├── schemas/
│   └── request.py           # Pydantic input/output schemas
├── services/
│   ├── knowledge_tracing.py # Business logic prediksi
│   └── generative_ai.py     # Gemini integration (Week 3)
├── utils/
│   └── preprocessing.py     # Preprocessing pipeline (konsisten dengan training)
└── saved_model/             # TF SavedModel artifacts