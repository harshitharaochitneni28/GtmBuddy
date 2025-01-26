# GtmBuddy

## Project Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Download spaCy model: `python -m spacy download en_core_web_sm`

## Running the Project
- Generate synthetic data: `python src/data_preparation.py`
- Train model: `python src/model_training.py`
- Run API: `python src/api.py`

## Docker Deployment
1. Build Docker image: `docker build -t sales-call-nlp .`
2. Run Docker container: `docker run -p 5000:5000 sales-call-nlp`

## API Usage
Send POST request to `/analyze` with JSON payload:
```json
{
  "text": "Sales call text snippet here"
}
