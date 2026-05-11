from transformers import pipeline

classifier = pipeline("sentiment-analysis")

texts = [
    "I love this product, it's amazing!",
    "This is the worst experience I've ever had.",
    "I'm not sure how I feel about this."
]

while True:
	text = input("Enter text (or type quit): ")
	if text.lower() == "quit":
		break
	result = classifier(text)
	print(f"Prediction: {result}\n")

