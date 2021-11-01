from io import StringIO
import json

from PIL.Image import Image
import compare_img
import cv2
import base64
# from typing import Coroutine
# from PIL import Image
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__,
            template_folder="../frontend/dist",
            static_folder="../frontend/dist/static")

CORS(app)

# @app.route('/')
# def hello_word():
#     return render_template("index.html")

# @app.route("/add", methods = ['POST'])
# def add_two_nums():
#     a = request.json.get('a')
#     b = request.json.get('b')
#     return json.dumps(
#         {
#             'data': a + b
#         }
#     )


@app.route("/search", methods=['POST'])
def search():
    imgUrl = request.json.get('imgUrl')
    # print('%s', imgUrl)
    img_b64code = imgUrl.replace('data:image/png;base64,', '')
    # print('%s', img_b64code)
    imgData = base64.b64decode(img_b64code)
    file = open('1.png', 'wb')
    file.write(imgData)
    file.close()
    # A,B图像的尺寸需要保持一致 （543，1430）（919，1430）
    imageA1 = cv2.imread('1.png')
    imageA = cv2.cvtColor(imageA1, cv2.COLOR_BGR2GRAY)
    imageB1 = cv2.imread('img/1.png')
    imageB = cv2.cvtColor(imageB1, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image', imageA)
    result = compare_img.compare_images(imageA, imageB, 'original_original')
    print(result)
    return json.dumps({'data': result})


if __name__ == '__main__':
    app.run()
