from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import numpy as np

app = Flask(__name__)

# Load the pre-trained BERT model
model = hub.load("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4")

def preprocess_text(text):
    # Basic text preprocessing
    text = text.lower().strip()
    return text

def get_embedding(text):
    # Get BERT embeddings
    preprocessed_text = preprocess_text(text)
    embeddings = model([preprocessed_text])
    return embeddings[0].numpy()

def analyze_sentiment(text):
    # This is a simplified sentiment analysis
    # In a real application, you would use a trained sentiment classifier
    positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'best']
    negative_words = ['bad', 'poor', 'terrible', 'sad', 'hate', 'worst']
    
    text = text.lower()
    positive_count = sum(1 for word in positive_words if word in text)
    negative_count = sum(1 for word in negative_words if word in text)
    
    if positive_count > negative_count:
        sentiment = 'positive'
        score = positive_count / (positive_count + negative_count)
    elif negative_count > positive_count:
        sentiment = 'negative'
        score = negative_count / (positive_count + negative_count)
    else:
        sentiment = 'neutral'
        score = 0.5
    
    return {
        'sentiment': sentiment,
        'score': float(score),
        'embedding': get_embedding(text).tolist()
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    result = analyze_sentiment(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 