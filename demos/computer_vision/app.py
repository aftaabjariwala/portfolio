from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
from model import ObjectDetector

app = Flask(__name__)

# Initialize the object detector
detector = ObjectDetector()
detection_active = False

def generate_frames():
    camera = cv2.VideoCapture(0)
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            if detection_active:
                # Get predictions
                predictions = detector.detect(frame)
                
                # Draw predictions on frame
                frame = detector.draw_predictions(frame, predictions)
            
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
    app.run(debug=True) 