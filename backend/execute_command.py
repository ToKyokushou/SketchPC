from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

import base64
import subprocess

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

    # do not have to import stdout
    ex = subprocess.Popen('sh execute_command.sh',
                          stderr=subprocess.PIPE, shell=True)
    stdout, stderr = ex.communicate()
    status = ex.wait()
    # print('cmd out: ', stdout.decode())
    f = open('./testData.txt')
    lines = f.readlines()
    # for line2 in lines:
    #     print(line2)
    return lines[0]

    # /home/du/iwaitPro/Database/SHREC12/Extended/D00261view/34.jpg


if __name__ == '__main__':
    app.run()
