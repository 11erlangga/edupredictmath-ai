from datetime import datetime, timezone

from schemas.predict import (
    Action,
    InterventionResponse,
    InterventionType,
    MasteryLevel,
    MetaResponse,
    NextStep,
    PredictData,
    PredictRequest,
    PredictResponse,
)
from services.gemini import generate_intervention_text

MODEL_VERSION = "dkt_v1"

# Threshold penguasaan konsep — masih menunggu keputusan DS untuk nilai yang fixed
THRESHOLD_LOW = 0.4
THRESHOLD_MEDIUM = 0.7


def get_mastery_and_action(
    probability: float,
) -> tuple[MasteryLevel, Action, NextStep, InterventionResponse | None]:
    if probability < THRESHOLD_LOW:
        return (
            MasteryLevel.low,
            Action.explain,
            NextStep.review,
            InterventionResponse(type=InterventionType.explanation),
        )
    elif probability < THRESHOLD_MEDIUM:
        return (
            MasteryLevel.medium,
            Action.hint,
            NextStep.retry,
            InterventionResponse(type=InterventionType.hint),
        )
    else:
        return (
            MasteryLevel.high,
            Action.next,
            NextStep.continue_,
            None,
        )


def predict_knowledge(request: PredictRequest) -> PredictResponse:
    # Dummy inference — nanti diganti model yang sudah di-train
    total = len(request.history)
    correct = sum([i.correctness for i in request.history])
    probability = correct / total

    mastery_level, action, next_step, intervention = get_mastery_and_action(probability)

    # Generate teks intervensi kalau mastery low/medium
    if intervention is not None:
        intervention.text = generate_intervention_text(
            intervention_type=intervention.type.value,
            concept_id=request.query_concept,
            interest=request.preferences.interest,
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
