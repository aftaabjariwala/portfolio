from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained BERT model
try:
    model = hub.load("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4")
except:
    # Fallback for deployment environments
    model = None

def preprocess_text(text):
    # Basic text preprocessing
    text = text.lower().strip()
    return text

def get_embedding(text):
    # Get BERT embeddings
    if model is None:
        # Fallback: return random embedding for demo
        return np.random.rand(768)
    
    preprocessed_text = preprocess_text(text)
    embeddings = model([preprocessed_text])
    return embeddings[0].numpy()

def analyze_sentiment(text):
    # This is a simplified sentiment analysis
    # In a real application, you would use a trained sentiment classifier
    positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'best', 'amazing', 'wonderful']
    negative_words = ['bad', 'poor', 'terrible', 'sad', 'hate', 'worst', 'awful', 'horrible']
    
    text = text.lower()
    positive_count = sum(1 for word in positive_words if word in text)
    negative_count = sum(1 for word in negative_words if word in text)
    
    if positive_count > negative_count:
        sentiment = 'positive'
        score = positive_count / (positive_count + negative_count + 1)
    elif negative_count > positive_count:
        sentiment = 'negative'
        score = negative_count / (positive_count + negative_count + 1)
    else:
        sentiment = 'neutral'
        score = 0.5
    
    return {
        'sentiment': sentiment,
        'score': float(score),
        'embedding': get_embedding(text).tolist()[:10]  # Return first 10 values for demo
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 