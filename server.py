from flask import Flask, request, jsonify
from transformers import pipeline
import torch

# Initialize Flask app
app = Flask(__name__)

# Load sentiment analysis model
model_name = "MarieAngeA13/Sentiment-Analysis-BERT"
model = pipeline("sentiment-analysis", model=model_name)


@app.route('/')
def home():
    return "Sentiment Analysis Model API"


@app.route('/analyze', methods=['POST'])
def analyze_text():
    if request.method == 'POST':
        data = request.json
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Perform sentiment analysis
        result = model(text)

        return jsonify(result)


if __name__ == "__main__":
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
