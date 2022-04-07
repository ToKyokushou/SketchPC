from flask import Flask, json, render_template, request, jsonify
from flask.templating import DispatchingJinjaLoader
from flask_cors import CORS
from PIL import Image
from matplotlib import pyplot as plt

import base64
import subprocess
import io
import cv2
import meshio
import numpy as np
import os
import pygalmesh
import dataio
import myICP


app = Flask(__name__,
            template_folder="../frontend/dist",
            static_folder="../frontend/dist/static")

CORS(app)


@app.route("/shell", methods=['POST'])
def shell():
    imgUrl = request.json.get('imgUrl')
    img_b64code = imgUrl.replace('data:image/png;base64,', '')
    imgData = base64.b64decode(img_b64code)
    file = open('1.png', 'wb')
    file.write(imgData)
    file.close()

    image_data = io.BytesIO(imgData)
    img = Image.open(image_data)
    w = img.width
    h = img.height
    img2 = img.crop((w/2-400, h/2-400, w/2+400, h/2+400))
    sp = img2.size
    width = sp[0]
    height = sp[1]
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = img2.getpixel(dot)
            if(color_d[3] == 0):
                color_d = (255, 255, 255)
                img2.putpixel(dot, color_d)
    imgByteArr = io.BytesIO()
    img2.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()
    file2 = open('1.jpg', 'wb')
    file2.write(imgByteArr)
    file2.close()

    # do not have to import stdout
    ex = subprocess.Popen('sh execute_command.sh',
                          stderr=subprocess.PIPE, shell=True)
    stdout, stderr = ex.communicate()
    status = ex.wait()
    f = open('./testData.txt')
    lines = f.readlines()

    # mesh = pygalmesh.remesh_surface(
    #     '/home/du/iwaitPro/SketchPC/frontend/static/threeDs/D00001.off',
    #     max_edge_size_at_feature_edges=0.025,
    #     min_facet_angle=25,
    #     max_radius_surface_delaunay_ball=0.1,
    #     max_facet_distance=0.001,
    #     verbose=False)
    # meshio.write('test.obj', mesh)

    # return lines[0]

    line = '0.282965 - /home/du/iwaitPro/experimentalData/D00103view/94.jpg'
    return line

    # /home/du/iwaitPro/Database/SHREC12/Extended/D00261view/34.jpg


@ app.route("/trans", methods=['POST'])
def trans():
    canvasData = request.json.get('canvasData')
    img_b64code = canvasData.replace('data:image/png;base64,', '')
    imgData = base64.b64decode(img_b64code)
    file = open('2.png', 'wb')
    file.write(imgData)
    file.close()

    # START: this part for threshold
    imgB = cv2.imread('./2.png')
    size = imgB.shape
    h = size[0]
    w = size[1]
    imgGray = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(imgGray, 217, 255, cv2.THRESH_BINARY)
    # ret, thresh2 = cv2.threshold(imgGray, 217, 255, cv2.THRESH_BINARY_INV)
    # ret, thresh3 = cv2.threshold(imgGray, 217, 255, cv2.THRESH_TRUNC)
    # ret, thresh4 = cv2.threshold(imgGray, 217, 255, cv2.THRESH_TOZERO)
    # ret, thresh5 = cv2.threshold(imgGray, 217, 255, cv2.THRESH_TOZERO_INV)
    # titles = ['Original Image', 'BINARY',
    #           'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    # images = [imgB, thresh1, thresh2, thresh3, thresh4, thresh5]
    # for i in range(6):
    #     plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')  # 避免灰度图彩色映射
    #     plt.title(titles[i])
    #     plt.xticks([]), plt.yticks([])  # 去掉刻度
    #     # plt.savefig("bigpic_2.png")
    # plt.show()
    # cv2.imshow('Original Image', imgB)
    # cv2.imshow('BINARY', thresh1)
    # cv2.imshow('BINARY_INV', thresh2)
    # cv2.imshow('TRUNC', thresh3)
    # cv2.imshow('TOZERO', thresh4)
    # cv2.imshow('TOZERO_INV', thresh5)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    contours, hier = cv2.findContours(
        thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    dst = np.ones(imgB.shape, dtype=np.uint8)
    file1 = cv2.drawContours(dst, contours, -1, (0, 255, 0), 1)
    fig = plt.figure(figsize=(36.88, 25.16))
    plt.plot(), plt.imshow(file1, 'gray')
    plt.xticks([]), plt.yticks([])
    plt.axis('off')
    path = ('./3.png')
    plt.savefig(path, dpi=100, bbox_inches='tight', pad_inches=0.0)
    # END: this part for threshold

    # function 1 START
    # img = cv2.imread('./2.png')
    # # cv2.imshow('original', img)
    # # rows, cols, ch = img.shape
    # size = img.shape
    # h = size[0]
    # w = size[1]
    # # print(h)
    # # print(w)
    # Ksize = 7
    # L2g = True
    # edge = cv2.Canny(img, 50, 100, apertureSize=Ksize, L2gradient=L2g)
    # contours, hierarchy = cv2.findContours(
    #     edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # dst = np.ones(img.shape, dtype=np.uint8)
    # file1 = cv2.drawContours(dst, contours, -1, (0, 255, 0), 1)
    # # cv2.imshow('dst', dst)
    # # cv2.waitKey()
    # fig = plt.figure(figsize=(36.88, 25.16))
    # plt.plot(), plt.imshow(file1)
    # plt.xticks([]), plt.yticks([])
    # plt.axis('off')
    # path = ('./3.png')
    # plt.savefig(path, dpi=100, bbox_inches='tight', pad_inches=0.0)
    # function 2 END

    # function 2 START : cv2.imshow error
    # image = cv2.imread("2.png")
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edged = cv2.Canny(gray, 50, 100)
    # cv2.imshow("Original", image)

    f = open('./3.png', 'rb')
    base64_data = f.read()
    image_data = io.BytesIO(base64_data)
    img4 = Image.open(image_data)
    # w = img4.width
    # h = img4.height
    # transform 3.png to 5.png, but don't have to do this
    # img5 = img4.crop((w/2-1844, h/2-1258, w/2+1844, h/2+1258))
    # imgByteArr = io.BytesIO()
    # img5.save(imgByteArr, format='PNG')
    # imgByteArr = imgByteArr.getvalue()
    # file5 = open('5.png', 'wb')
    # file5.write(imgByteArr)
    # file5.close()

    # transform 3.png to 4.png, but 0.5 size of 2.png
    # img2 = Image.open(image_data)
    img2 = img4.resize((int(w/2), int(h/2)), Image.ANTIALIAS)
    width = img2.width
    height = img2.height
    sp = img2.size
    width = sp[0]
    height = sp[1]
    # img3 = img2.crop((width/2-922, height/2-629,
    #                  width/2+922, height/2+629))
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = img2.getpixel(dot)
            if(color_d[0] != 0):
                color_d = (255, 255, 255, 0)
                img2.putpixel(dot, color_d)
            if(color_d[0] == 0):
                color_d = (0, 0, 0, 255)
                img2.putpixel(dot, color_d)
    imgByteArr = io.BytesIO()
    # img3.save(imgByteArr, format='PNG')
    img2.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()
    file3 = open('4.png', 'wb')
    file3.write(imgByteArr)
    file3.close()
    return 'aaa'


@ app.route("/getBase", methods=['POST'])
def getBase():
    f = open('./4.png', 'rb')
    head = bytes('data:image/png;base64,', 'utf-8')
    base64_data = base64.b64encode(f.read())
    base = head + base64_data
    return base


@ app.route("/iteration", methods=['POST'])
def iteration():
    targetFile = request.json.get('target')
    originalFile = request.json.get('original')
    print('json file name')
    print(targetFile)
    print(originalFile)
    print('start load json file')
    targetData = dataio.loadJson(
        '/home/du/iwaitPro/SketchPC/frontend/static/threeDs/'+targetFile)
    originalData = dataio.loadJson(
        '/home/du/iwaitPro/SketchPC/frontend/static/threeDs/'+originalFile+'.json')
    _, _, originalData2 = myICP.icp(originalData, targetData, maxIteration=30,
                                    tolerance=0.000001, controlPoints=3000)
    fileName = dataio.outputICP(originalFile, originalData2)
    return fileName


if __name__ == '__main__':
    app.run()
