from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    result = sentiment_analyzer(text)
    return jsonify(result[0])

if __name__ == '__main__':
    app.run(port=5000)
