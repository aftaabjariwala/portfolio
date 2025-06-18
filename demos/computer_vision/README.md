# Real-time Object Detection Demo

A real-time object detection demo using TensorFlow and OpenCV. This project demonstrates how to build and deploy a computer vision application using Flask.

## Features

- Real-time object detection using webcam feed
- Pre-trained MobileNetV2 model for ImageNet classification
- Interactive web interface
- Start/Stop detection controls
- Real-time confidence scores

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aftaabjariwala/computer-vision-demo.git
cd computer-vision-demo
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:

```bash
python app.py
```

2. Open your browser and navigate to:

```
http://localhost:5000
```

3. Click "Start Detection" to begin real-time object detection.

## Project Structure

```
computer-vision-demo/
├── app.py              # Flask application
├── model.py            # Object detection model
├── requirements.txt    # Project dependencies
├── templates/          # HTML templates
│   └── index.html     # Main interface
└── README.md          # Project documentation
```

## Technologies Used

- Python 3.8+
- TensorFlow 2.7.0
- OpenCV 4.5.3
- Flask 2.0.1
- MobileNetV2 (pre-trained model)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Aftaab Jariwala - [LinkedIn](https://www.linkedin.com/in/aftaab-jariwala/)
