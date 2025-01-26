import os
import random
import json

def generate_synthetic_data(num_samples=100):
    # Get absolute path of the project directory
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(project_dir, 'data')
    
    # Create data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)

    domain_knowledge = {
        "competitors": ["CompetitorX", "CompetitorY", "CompetitorZ"],
        "features": ["analytics", "AI engine", "data pipeline"],
        "pricing_keywords": ["discount", "renewal cost", "budget"]
    }
    
    label_options = [
        "Objection", "Pricing Discussion", "Security", 
        "Competition", "Technical Discussion", "Positive"
    ]
    
    data = []
    
    templates = [
        "We love the {feature}, but {competitor} has a cheaper subscription.",
        "Our team is worried about {security_concern}.",
        "Your {feature} seems impressive compared to others.",
        "Can we discuss {pricing_keyword} for our deployment?",
        "We're concerned about {security_concern} and integration."
    ]
    
    for idx in range(1, num_samples + 1):
        template = random.choice(templates)
        
        snippet = template.format(
            feature=random.choice(domain_knowledge['features']),
            competitor=random.choice(domain_knowledge['competitors']),
            security_concern="data privacy",
            pricing_keyword=random.choice(domain_knowledge['pricing_keywords'])
        )
        
        num_labels = random.randint(1, 3)
        labels = ','.join(random.sample(label_options, num_labels))
        
        data.append({
            'id': idx,
            'text_snippet': snippet,
            'labels': labels
        })
    
    # Save dataset with absolute path
    dataset_path = os.path.join(data_dir, 'calls_dataset.json')
    knowledge_path = os.path.join(data_dir, 'domain_knowledge.json')
    
    with open(dataset_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    with open(knowledge_path, 'w') as f:
        json.dump(domain_knowledge, f, indent=2)

if __name__ == "__main__":
    generate_synthetic_data()