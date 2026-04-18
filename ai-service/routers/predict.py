from fastapi import APIRouter
from schemas.predict import PredictRequest, PredictResponse
from services.inference import predict_knowledge

router = APIRouter(prefix="/predict", tags=["Prediction"])


@router.post(
    "/",
    response_model=PredictResponse,
    summary="Prediksi penguasaan konsep siswa",
    description="Menerima riwayat interaksi siswa dan mengembalikan prediksi penguasaan konsep beserta rekomendasi tindakan.",
)
def predict(request: PredictRequest):
    return predict_knowledge(request)
