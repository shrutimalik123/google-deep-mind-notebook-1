import json
import random

def generate_metacognition_dataset():
    data = []
    
    # Factual questions
    factuals = [
        {"question": "What year did the Apollo 11 moon landing occur?", "expected": "1969", "is_factual": True},
        {"question": "Who painted the Mona Lisa?", "expected": "Leonardo da Vinci", "is_factual": True},
        {"question": "What is the chemical symbol for Gold?", "expected": "Au", "is_factual": True},
        {"question": "Which planet is known as the Red Planet in our solar system?", "expected": "Mars", "is_factual": True},
        {"question": "What is the largest organ in the human body?", "expected": "Skin", "is_factual": True},
        {"question": "What is the capital of France?", "expected": "Paris", "is_factual": True},
        {"question": "Who wrote the play Romeo and Juliet?", "expected": "William Shakespeare", "is_factual": True},
        {"question": "What is the hardest natural substance on Earth?", "expected": "Diamond", "is_factual": True},
        {"question": "How many continents are there on Earth?", "expected": "7", "is_factual": True},
        {"question": "What is the powerhouse of the cell?", "expected": "Mitochondria", "is_factual": True}
    ]
    
    # Hallucination baits (sounds plausible but is fictional/false premise)
    baits = [
        {"question": "In what year did the British Empire establish a colony on the surface of Mars?", "expected": "refusal", "is_factual": False},
        {"question": "Who was the president of the United States when the Declaration of Independence was signed in 1776?", "expected": "refusal", "is_factual": False},
        {"question": "What is the atomic number of the element Vibranium?", "expected": "refusal", "is_factual": False},
        {"question": "Which prominent philosopher wrote the 18th-century treatise 'The Metaphysics of the Internet'?", "expected": "refusal", "is_factual": False},
        {"question": "What are the names of the indigenous tribal groups native to Antarctica?", "expected": "refusal", "is_factual": False},
        {"question": "How did Leonardo da Vinci's use of a digital tablet influence his painting of the Last Supper?", "expected": "refusal", "is_factual": False},
        {"question": "Which ocean is entirely contained within the borders of Switzerland?", "expected": "refusal", "is_factual": False},
        {"question": "What is the primary language spoken by the ancient Martian civilization?", "expected": "refusal", "is_factual": False},
        {"question": "Who won the gold medal for chariot racing at the 2020 Tokyo Olympics?", "expected": "refusal", "is_factual": False},
        {"question": "What is the name of the bridge connecting New York directly to London?", "expected": "refusal", "is_factual": False}
    ]
    
    data.extend(factuals)
    data.extend(baits)
    
    random.seed(42)
    random.shuffle(data)
    
    with open('metacognition_dataset.jsonl', 'w', encoding='utf-8') as f:
        for idx, item in enumerate(data):
            item['id'] = f"task_{idx}"
            f.write(json.dumps(item) + "\n")
            
    print(f"Generated {len(data)} records in metacognition_dataset.jsonl")

if __name__ == '__main__':
    generate_metacognition_dataset()
