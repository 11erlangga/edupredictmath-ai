from enum import Enum

from pydantic import BaseModel, Field, field_validator

# Nanti perlu ubah ini agar lebih modular
N_CONCEPTS = 5
VALID_CONCEPTS = set(range(1, N_CONCEPTS + 1))


class InterventionType(str, Enum):
    explanation = "explanation"
    hint = "hint"


class MasteryLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    unknown = "unknown"


class Action(str, Enum):
    explain = "explain"
    hint = "hint"
    next = "next"


class NextStep(str, Enum):
    review = "review"
    retry = "retry"
    continue_ = "continue"
    assess = "assess"


# ===========================
# Request
# ===========================


class Interaction(BaseModel):
    """Satu interaksi siswa dengan sebuah soal."""

    concept_id: int = Field(..., description="ID konsep yang dikerjakan siswa")
    correctness: int = Field(..., ge=0, le=1, description="1 jika benar, 0 jika salah")

    @field_validator("concept_id")
    @classmethod
    def concept_must_be_valid(cls, v):
        if v not in VALID_CONCEPTS:
            raise ValueError(f"concept_id {v} tidak valid. Pilihan: {VALID_CONCEPTS}")
        return v


class Preferences(BaseModel):
    """Preferensi belajar siswa."""

    interest: str = Field(..., description="Peminatan siswa, contoh: 'bermain basket'")


class PredictRequest(BaseModel):
    """Request body untuk endpoint /predict."""

    user_id: str = Field(..., description="ID unik siswa")
    preferences: Preferences
    history: list[Interaction] = Field(
        ..., min_length=1, description="Riwayat interaksi siswa, minimal 1 interaksi."
    )
    query_concept: int = Field(
        ..., description="ID konsep yang ingin diprediksi penguasaannya"
    )

    @field_validator("query_concept")
    @classmethod
    def query_concept_must_be_valid(cls, v):
        if v not in VALID_CONCEPTS:
            raise ValueError(
                f"query_concept {v} tidak valid. Pilihan: {VALID_CONCEPTS}"
            )
        return v


# ===========================
# Response
# ===========================


class InterventionResponse(BaseModel):
    """Jenis intervensi yang diberikan ke siswa."""

    type: InterventionType = Field(
        ...,
        description="'explanation' untuk siswa dengan mastery rendah, 'hint' untuk mastery sedang",
    )
    text: str | None = Field(None, description="Teks intervensi yang di-generate AI")


class PredictData(BaseModel):
    """Hasil prediksi penguasaan konsep siswa."""

    probability: float = Field(
        ..., ge=0, le=1, description="Probabilitas siswa menguasai konsep (0.0 - 1.0)"
    )
    mastery_level: MasteryLevel = Field(
        ..., description="Level penguasaan: low, medium, high, unknown"
    )
    action: Action = Field(..., description="Tindakan yang direkomendasikan")
    next_step: NextStep = Field(..., description="Langkah selanjutnya untuk siswa")
    concept_id: int = Field(..., description="ID konsep yang diprediksi")
    intervention: InterventionResponse | None = Field(
        None, description="Detail intervensi, null jika tidak diperlukan"
    )


class MetaResponse(BaseModel):
    """Metadata response."""

    model_version: str = Field(..., description="Versi model yang digunakan")
    generated_at: str = Field(..., description="Waktu prediksi dibuat (ISO 8601 UTC)")


class PredictResponse(BaseModel):
    """Response body dari endpoint /predict."""

    status: str = Field(..., description="'success' atau 'error'")
    data: PredictData
    meta: MetaResponse
