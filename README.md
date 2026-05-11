# Sentiment Analysis Project

A simple sentiment analysis tool built with HuggingFace Transformers and Python.  
Runs locally on Oracle Linux (WSL) using a virtual environment.

## Features
- Uses DistilBERT sentiment analysis model
- Interactive CLI mode (type text and get predictions)
- Clean project structure
- Easy to run and extend
- FastApi endpoint for real-time ML inference
- Virtual environment isolation (Oracle Linux WSL)
## How to Run

### 1. Activate environment
source ~/ai-env/bin/activate

### 2. Install dependencies:
pip install -r requirement.txt
### 3. Run the script
python src/sentiment.py

### 4. Enter text
Type any sentence and get a sentiment prediction.

### 5. Exit
Type `quit` to exit.
Closes CLI tool
## Tech Stack
- Python
- HuggingFace Transformers
- DistilBERT 
- Oracle Linux (WSL)
- FastAPI
- Uvicorn
