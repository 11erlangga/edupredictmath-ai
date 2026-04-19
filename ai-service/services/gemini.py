import os

from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

PROMPT_EXPLANATION = """
Kamu adalah tutor matematika yang kreatif dan suportif.
Siswa ini menyukai: {interest}.
Mereka kesulitan memahami {concept_name}.
Berikan penjelasan singkat (2-3 kalimat) menggunakan analogi dari {interest}.
Gunakan bahasa yang santai dan mudah dipahami.
"""

PROMPT_HINT = """
Kamu adalah tutor matematika.
Siswa ini menyukai: {interest}.
Mereka sedang mengerjakan soal tentang {concept_name}.
Berikan 1 hint singkat (1-2 kalimat) tanpa langsung memberi jawaban.
Kaitkan dengan {interest} jika memungkinkan.
"""


def generate_intervention_text(
    intervention_type: str,
    concept_id: int,
    interest: str,
) -> str:
    concept_name = f"Konsep {concept_id}"

    if intervention_type == "explanation":
        prompt = PROMPT_EXPLANATION.format(concept_name=concept_name, interest=interest)
    else:
        prompt = PROMPT_HINT.format(concept_name=concept_name, interest=interest)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
