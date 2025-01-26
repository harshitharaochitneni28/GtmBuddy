import json
import re

class EntityExtractor:
    def __init__(self, domain_knowledge_path='data/domain_knowledge.json'):
        with open(domain_knowledge_path, 'r') as f:
            self.domain_knowledge = json.load(f)
    
    def extract_entities(self, text):
        text_lower = text.lower()
        entities = {
            'competitors': [],
            'features': [],
            'pricing_keywords': []
        }
        
        # Dictionary-based extraction
        for category, keywords in self.domain_knowledge.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    entities[category].append(keyword)
        
        # Basic regex-based extraction
        numeric_patterns = {
            'pricing_keywords': r'\$?(\d+(?:\.\d+)?)',
            'percentages': r'(\d+)%'
        }
        
        for key, pattern in numeric_patterns.items():
            matches = re.findall(pattern, text)
            if matches:
                entities[key].extend(matches)
        
        return entities

def main():
    extractor = EntityExtractor()
    test_texts = [
        "We're considering CompetitorX for their AI analytics platform",
        "Looking for a solution with pricing under $5000",
        "Interested in 20% discount for annual subscription"
    ]
    
    for text in test_texts:
        print(f"Text: {text}")
        print("Extracted Entities:", extractor.extract_entities(text), "\n")

if __name__ == "__main__":
    main()