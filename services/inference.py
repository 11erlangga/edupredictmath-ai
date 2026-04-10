from datetime import datetime, timezone

from schemas.predict import (
    InterventionResponse,
    MetaResponse,
    PredictData,
    PredictRequest,
    PredictResponse,
)

MODEL_VERSION = "dkt_v1"


def get_mastery_and_action(probability: float, no_history: bool):
    if no_history:
        return "unknown", "next", "assess", None

    if probability < 0.4:  # tunggu keputusan tim ds buat threshold yang fixed
        return "low", "explain", "review", InterventionResponse(type="explanation")
    elif probability < 0.7:  # tunggu keputusan tim ds buat threshold yang fixed
        return "medium", "hint", "retry", InterventionResponse(type="hint")
    else:
        return "high", "next", "continue", None


def predict_knowledge(request: PredictRequest) -> PredictResponse:
    no_history = len(request.history) == 0

    if no_history:
        probability = 0.5
    else:
        # Dummy inference — nanti diganti model DKT asli
        total = len(request.history)
        correct = sum([i.correctness for i in request.history])
        probability = correct / total

    mastery_level, action, next_step, intervention = get_mastery_and_action(
        probability, no_history
    )

    return PredictResponse(
        status="success",
        data=PredictData(
            probability=probability,
            mastery_level=mastery_level,
            action=action,
            next_step=next_step,
            concept_id=request.query_concept,
            intervention=intervention,
        ),
        meta=MetaResponse(
            model_version=MODEL_VERSION,
            generated_at=datetime.now(timezone.utc).isoformat(),
        ),
    )
