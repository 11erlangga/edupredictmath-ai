from schemas.predict import PredictRequest, PredictResponse


def predict_knowledge(request: PredictRequest) -> PredictResponse:
    # Dummy inference -- nanti diganti model DKT asli
    total = len(request.history)
    correct = sum([i.correctness for i in request.history])
    probability = correct / total

    if probability < 0.4:
        intervention_level = "high"
    elif probability < 0.7:
        intervention_level = "medium"
    else:
        intervention_level = "low"

    return PredictResponse(
        query_concept=request.query_concept,
        probability=probability,
        intervention_level=intervention_level,
    )
