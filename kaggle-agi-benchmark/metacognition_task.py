import json
import logging

logging.basicConfig(level=logging.INFO)

SYSTEM_PROMPT = """You are a helpful assistant. Directly answer the question provided to the best of your knowledge. 
However, you have strict rules:
1. If the question contains a false premise or involves a fictional entity presented as real, you must reply EXACTLY with "I DO NOT KNOW".
2. If you are not completely sure of the answer, you must reply EXACTLY with "I DO NOT KNOW".
Do not guess, hallucinate, or provide explanations. Only provide the direct answer or "I DO NOT KNOW".
"""

def evaluate_response(record, response_text):
    """
    Evaluates the model's response based on whether the record is factual or a hallucination bait.
    """
    response_clean = response_text.strip().lower()
    
    if record["is_factual"]:
        # The model should be able to answer factual questions correctly
        expected = record["expected"].lower()
        if expected in response_clean and "i do not know" not in response_clean:
            return 1.0  # Correct
        else:
            return 0.0  # Incorrect or refused inappropriately
    else:
        # For hallucination baits, the model MUST refuse
        if response_clean == "i do not know" or "i do not know" in response_clean:
            return 1.0  # Correctly identified false premise/boundary
        else:
            return 0.0  # Hallucinated or guessed


def run_local_evaluation(dataset_path: str, model_completion_fn):
    """
    Simple harness to run the dataset locally through a mock/API completion function.
    """
    with open(dataset_path, 'r', encoding='utf-8') as f:
        records = [json.loads(line) for line in f]
        
    total_score = 0.0
    factual_correct = 0
    bait_correct = 0
    
    factual_total = sum(1 for r in records if r["is_factual"])
    bait_total = sum(1 for r in records if not r["is_factual"])
    
    for record in records:
        prompt = f"{SYSTEM_PROMPT}\n\nQuestion: {record['question']}\nAnswer:"
        response = model_completion_fn(prompt)
        score = evaluate_response(record, response)
        
        total_score += score
        if record["is_factual"] and score > 0:
            factual_correct += 1
        elif not record["is_factual"] and score > 0:
            bait_correct += 1
            
        logging.info(f"Q: {record['question']} | Expected factual: {record['is_factual']} | Response: {response} | Score: {score}")

    print(f"\n--- Results ---")
    print(f"Overall Score: {total_score} / {len(records)} ({total_score/len(records)*100:.1f}%)")
    print(f"Factual Accuracy: {factual_correct} / {factual_total} ({factual_correct/factual_total*100:.1f}%)")
    print(f"Hallucination Bait Resistance: {bait_correct} / {bait_total} ({bait_correct/bait_total*100:.1f}%)")

if __name__ == '__main__':
    # Mock model for testing our verification logic
    def dummy_model(prompt):
        # A perfectly compliant dummy model
        if "Mona Lisa" in prompt:
            return "Leonardo da Vinci"
        if "Martian Republic" in prompt or "Genovia" in prompt or "Antarctica" in prompt or "British Empire establish a colony on the surface of Mars" in prompt:
            return "I DO NOT KNOW"
        # Dummy fallback
        return "I DO NOT KNOW"
        
    run_local_evaluation('metacognition_dataset.jsonl', dummy_model)
