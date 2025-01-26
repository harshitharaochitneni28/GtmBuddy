import json
import random
import re

class BasicClassifier:
    def __init__(self):
        self.keywords = {
            'Pricing Discussion': ['price', 'cost', 'budget', 'discount'],
            'Security': ['security', 'privacy', 'compliance', 'data protection'],
            'Competition': ['competitor', 'alternative', 'vs', 'comparison'],
            'Technical Discussion': ['feature', 'technology', 'platform', 'integration'],
            'Objection': ['concern', 'problem', 'issue', 'but'],
            'Positive': ['love', 'impressive', 'great', 'good']
        }
    
    def preprocess_text(self, text):
        # Convert to lowercase, remove special characters
        return re.sub(r'[^a-z\s]', '', text.lower())
    
    def predict_labels(self, text):
        processed_text = self.preprocess_text(text)
        predicted_labels = []
        
        for label, keywords in self.keywords.items():
            if any(keyword in processed_text for keyword in keywords):
                predicted_labels.append(label)
        
        return predicted_labels if predicted_labels else ['Neutral']
    
    def train(self, dataset_path='data/calls_dataset.json'):
        with open(dataset_path, 'r') as f:
            dataset = json.load(f)
        
        # Basic training (keyword refinement could be added here)
        return dataset

def main():
    classifier = BasicClassifier()
    dataset = classifier.train()
    
    # Simple evaluation
    print("Sample Predictions:")
    test_texts = [
        "We want to discuss pricing for our deployment",
        "Your security features look impressive",
        "How does your solution compare to competitors?"
    ]
    
    for text in test_texts:
        predictions = classifier.predict_labels(text)
        print(f"Text: {text}")
        print(f"Predicted Labels: {predictions}\n")

if __name__ == "__main__":
    main()