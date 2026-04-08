def get_intervention_level(probability: float) -> str:
    if probability < 0.4:
        return "high"
    elif probability < 0.7:
        return "medium"
    else:
        return "low"
