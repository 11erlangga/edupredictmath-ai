from pydantic import BaseModel, Field, field_validator

VALID_CONCEPTS = {1, 2, 3, 4, 5}


class Interaction(BaseModel):
    concept_id: int
    correctness: int = Field(..., ge=0, le=1)

    @field_validator("concept_id")
    @classmethod
    def concept_must_be_valid(cls, v):
        if v not in VALID_CONCEPTS:
            raise ValueError(f"concept_id {v} tidak valid. Pilihan: {VALID_CONCEPTS}")
        return v


class PredictRequest(BaseModel):
    history: list[Interaction]
    query_concept: int

    @field_validator("history")
    @classmethod
    def history_must_not_be_empty(cls, v):
        if len(v) == 0:
            raise ValueError("history tidak boleh kosong")
        return v

    @field_validator("query_concept")
    @classmethod
    def query_concept_must_be_valid(cls, v):
        if v not in VALID_CONCEPTS:
            raise ValueError(
                f"query_concept {v} tidak valid. Pilihan: {VALID_CONCEPTS}"
            )
        return v


class PredictResponse(BaseModel):
    query_concept: int
    probability: float
    intervention_level: str
