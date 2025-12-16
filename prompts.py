from dataclasses import dataclass
from typing import List, Literal

Audience = Literal["medical", "patient", "one_sentence"]

@dataclass
class ECGResult:
    rhythm: str                 # e.g., "Atrial Fibrillation"
    confidence: float           # 0~1
    features: List[str]         # e.g., ["Irregular RR intervals", "No visible P waves"]

def build_prompt(result: ECGResult, audience: Audience) -> str:
    # 共通規則（很重要：避免「醫療診斷/治療」高風險措辭）
    common_rules = """
Rules:
- Do NOT provide a medical diagnosis or treatment instructions.
- Avoid deterministic or alarming language.
- Use informational, educational tone only.
- If uncertain, say it is an AI-generated interpretation and suggest professional evaluation.
"""

    # 依不同受眾調整風格（這就是 condition）
    if audience == "medical":
        style = """
Target: Clinician (medical explanation)
- Use precise clinical terminology.
- Mention key ECG patterns and how they relate to the predicted rhythm.
- Keep it concise (80-140 words).
"""
    elif audience == "patient":
        style = """
Target: General patient (patient-friendly explanation)
- Use simple, reassuring language.
- Avoid medical jargon; explain terms if needed.
- Keep it short (80-140 words).
- Focus on what the pattern might suggest, not a diagnosis.
"""
    else:  # one_sentence
        style = """
Target: Non-medical user (one-sentence summary)
- Output EXACTLY one sentence.
- Very simple wording.
- No scary wording.
"""

    # 把模型輸出「結構化」放進 prompt（condition input）
    content = f"""
ECG model output (structured):
- Predicted rhythm: {result.rhythm}
- Confidence: {result.confidence:.0%}
- Key observed characteristics:
{chr(10).join([f"  - {x}" for x in result.features])}
"""

    return f"""You are a helpful assistant that generates ECG result explanations.

{common_rules}
{style}
{content}

Now generate the explanation:
"""
