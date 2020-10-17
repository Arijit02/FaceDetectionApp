from os import path
import cv2
import numpy as np
from flask import Flask, request, Response
import uuid
import json

# Face Detection Function


def detectFace(img):
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(img_gray, 1.3, 5)

    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)

    # Save File
    path_file = ('static/%s.jpg' % uuid.uuid4().hex)
    cv2.imwrite(path_file, img)

    return json.dumps(path_file)    # Return image file name as json


# API
app = Flask(__name__)


# route http post to this method
@app.route('/api/upload', methods=['POST'])
def upload():
    # Retrieve image from client
    img = cv2.imdecode(np.fromstring(
        request.files['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Processing image
    img_processed = detectFace(img)

    # Return json string
    return Response(response=img_processed, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run()
