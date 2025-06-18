from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
from model import ObjectDetector
import os

app = Flask(__name__)

# Initialize the object detector
detector = ObjectDetector()
detection_active = False

def generate_frames():
    # For deployment, we'll use a sample image instead of camera
    # In production, you might want to use a webcam or uploaded images
    sample_image = np.ones((480, 640, 3), dtype=np.uint8) * 50
    
    while True:
        if detection_active:
            # Get predictions on sample image
            predictions = detector.detect(sample_image)
            frame = detector.draw_predictions(sample_image, predictions)
        else:
            frame = sample_image.copy()
            # Add text to indicate demo mode
            cv2.putText(frame, "Demo Mode - No Camera", (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 157), 2)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_detection')
def start_detection():
    global detection_active
    detection_active = True
    return jsonify({'status': 'success', 'message': 'Detection started'})

@app.route('/stop_detection')
def stop_detection():
    global detection_active
    detection_active = False
    return jsonify({'status': 'success', 'message': 'Detection stopped'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 