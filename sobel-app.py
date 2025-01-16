import cv2
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# 處理影像的 API
@app.route('/process', methods=['POST'])
def process_image():
    file = request.files['image']
    np_img = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_GRAYSCALE)

    # Sobel 運算
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)

    _, buf = cv2.imencode('.png', sobel_combined)
    return buf.tobytes(), 200, {'Content-Type': 'image/png'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
from dapr.clients import DaprClient

@app.route('/publish', methods=['POST'])
def publish_result():
    file = request.files['image']
    with DaprClient() as client:
        client.publish_event(
            pubsub_name="message-bus",
            topic_name="sobel-results",
            data=file.read()
        )
    return "Message published!", 200

