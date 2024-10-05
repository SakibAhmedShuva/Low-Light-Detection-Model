from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def check_light(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    avg_brightness = cv2.mean(hsv[:, :, 2])[0]
    if avg_brightness < 100:
        return False
    else:
        return True

@app.route('/check_light', methods=['POST'])
def check_light_endpoint():
    data = request.get_json()
    img_data = data['image']
    img_bytes = base64.b64decode(img_data)
    np_arr = np.frombuffer(img_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    light_status = check_light(image)
    return jsonify({'light_status': light_status})

if __name__ == '__main__':
    app.run(debug=True)
