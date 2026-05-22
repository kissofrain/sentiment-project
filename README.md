# sentiment-project

Basic sentiment analysis project.  
Uses HuggingFace’s DistilBERT model.  
Runs through CLI, FastAPI, and a Gradio UI.

---

## Overview
Started as a simple sentiment tool. Expanded it into a small ML stack:
- Transformers pipeline (DistilBERT)
- FastAPI endpoint
- Gradio UI for real-time testing
- CPU-only Torch setup (Oracle Linux WSL)

Keeping everything lightweight and local.

---

## Features
- Sentiment analysis using `distilbert-base-uncased-finetuned-sst-2-english`
- CLI script for quick checks
- FastAPI server for programmatic access
- Gradio UI for interactive testing
- Logs stored in `flagged/log.csv` (future use)
---
## Tech Stack
- Python  
- HuggingFace Transformers  
- DistilBERT  
- PyTorch (CPU)  
- FastAPI  
- Uvicorn  
- Gradio  
- Oracle Linux (WSL)
---
## Features

---
## Installation
Create a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
pip -install torch --index-url https://download.pytorch.org/whl/cpu


---

## Running the Project

### Gradio UI (main entry point)

python src/ui.py

Runs on:
http://127.0.0.1:7860


### FastAPI Server
uvicorn src.api:app --reload

#example request
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "All feedback is appreciated!"}'
#CLI Script
python src/sentiment.py "your text here"

---
#Project Structure
sentiment-project/
│
├── README.md
├── requirements.txt
├── flagged/
│   └── log.csv
│
└── src/
    ├── sentiment.py      # CLI entry point
    ├── api.py            # FastAPI server
    ├── ui.py             # Gradio interface
    └── model/
        └── loader.py     # Model loading utilities



### CLI Script
python src/sentiment.py "write something here"


