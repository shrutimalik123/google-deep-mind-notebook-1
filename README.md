# Kaggle: Measuring Progress Toward AGI - Metacognition Track

This repository contains the benchmark and submission assets for the **Google DeepMind - Measuring Progress Toward AGI** hackathon. 

The project focuses on the **Metacognition** track, specifically isolating a model's ability to recognize the boundaries of its factual knowledge and resist hallucinating in the face of false premises.

## Team Details
- **Team Name:** Shruti Malik
- **Affiliation:** Hobby Researcher

## Project Structure
- `kaggle-agi-benchmark/`
  - `metacognition_task.py`: The core evaluation script with a local test harness.
  - `metacognition_dataset.jsonl`: A curated dataset of 20 factual and "hallucination bait" questions.
  - `generate_dataset.py`: Utility script used to generate the evaluation data.
  - `kaggle_thumbnail.png`: Custom-designed thumbnail for the Kaggle writeup.
  - `eval_video.mp4`: Recorded demonstration of the benchmark execution.
  - `detailed_eval_video.mp4`: An enhanced recording featuring on-screen explanations and scrolling.

## How to Run the Evaluation
To see the benchmark in action locally:
1. Navigate to the project directory: `cd kaggle-agi-benchmark`
2. Run the evaluation script: `python metacognition_task.py`

## Benchmark Methodology
Our approach enforces a strict system prompt requiring the model to output "I DO NOT KNOW" when encountering fictional entities presented as real. The scoring logic rewards both accurate factual recall and successful refusal of false premises, revealing the "metacognitive gap" in frontier models.

## Submission Artifacts
The full Kaggle report and detailed process walkthrough are located in the `.gemini/antigravity/brain/` directory:
- [Kaggle Writeup](file:///C:/Users/Owner/.gemini/antigravity/brain/373a8495-a665-4fa2-84e2-4651a0c49928/kaggle_writeup.md)
- [Project Walkthrough](file:///C:/Users/Owner/.gemini/antigravity/brain/373a8495-a665-4fa2-84e2-4651a0c49928/walkthrough.md)
