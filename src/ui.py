import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze(text):
    result = classifier(text)[0]
    return f"{result['label']} ({result['score']:.4f})"

demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(label="Enter text"),
    outputs=gr.Textbox(label="Sentiment"),
    title="Sentiment Analyzer",
    description="Real-time sentiment analysis using DistilBERT + HuggingFace."
)

if __name__ == "__main__":
    demo.launch()
