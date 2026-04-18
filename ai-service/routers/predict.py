from fastapi import APIRouter

from schemas.predict import PredictRequest, PredictResponse
from services.inference import predict_knowledge

router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    return predict_knowledge(request)
