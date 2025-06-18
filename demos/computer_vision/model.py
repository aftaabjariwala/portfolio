import tensorflow as tf
import numpy as np
import cv2

class ObjectDetector:
    def __init__(self, model_path=None):
        if model_path:
            self.model = tf.keras.models.load_model(model_path)
        else:
            # Load a pre-trained model for demo purposes
            self.model = tf.keras.applications.MobileNetV2(
                input_shape=(224, 224, 3),
                include_top=True,
                weights='imagenet'
            )
        
        # Load ImageNet class names
        self.class_names = tf.keras.applications.mobilenet_v2.decode_predictions

    def preprocess_image(self, image):
        # Resize and preprocess image for MobileNetV2
        image = cv2.resize(image, (224, 224))
        image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
        return np.expand_dims(image, axis=0)

    def detect(self, image):
        # Preprocess image
        processed_image = self.preprocess_image(image)
        
        # Get predictions
        predictions = self.model.predict(processed_image)
        
        # Decode predictions
        decoded_predictions = self.class_names(predictions, top=3)[0]
        
        # Format results
        results = []
        for _, label, confidence in decoded_predictions:
            results.append({
                'label': label,
                'confidence': float(confidence)
            })
        
        return results

    def draw_predictions(self, image, predictions):
        # Create a copy of the image for drawing
        output_image = image.copy()
        
        # Draw predictions
        y_offset = 30
        for pred in predictions:
            text = f"{pred['label']}: {pred['confidence']:.2f}"
            cv2.putText(output_image, text, (10, y_offset),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            y_offset += 30
        
        return output_image 