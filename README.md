# ECG AIGC Explainer

This project demonstrates an **ECG-based AIGC system** that generates
**multi-level natural language explanations** (Medical / Patient-friendly / One-sentence)
from structured ECG analysis results using **conditional text generation**.

## Overview
- Input: Sample ECG (demo)
- Analysis: Structured ECG model output (rhythm, confidence, features)
- Generation: Conditional prompt-based text generation
- Interface: Streamlit web application

## Features
- Multi-level explanation generation:
  - Medical explanation for clinicians
  - Patient-friendly explanation for general users
  - One-sentence summary for non-medical users
- Prompt transparency for report and agent log
- Fallback generation when API quota is unavailable

## Project Structure
ecg-aigc-explainer/
├─ app.py
├─ prompts.py
├─ llm.py
├─ requirements.txt
├─ README.md
└─ .gitignore

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py