import numpy as np
import json


def loadData(fileName):
    fin = open(fileName, "r")
    lines = fin.readlines()
    cnt = len(lines)
    data = np.zeros([cnt, 3])
    for i in range(2, cnt):
        data[i - 2] = lines[i].split(' ')
    fin.close()
    return data


def outputData(fileName, data):
    fout = open(fileName, "w")
    for i in range(data.shape[0]):
        fout.write(str(data[i][0]) + ',' + str(data[i]
                   [1]) + ',' + str(data[i][2]) + '\n')
    fout.close()


def loadJson(fileName):
    fin = open(fileName, "r")
    data = json.load(fin)
    cnt = len(data['point_set'])
    print(cnt)
    # print(data['point_set'])
    # point_set = data['point_set']
    # lines = fin.readlines()
    # cnt = len(lines)
    # data = np.zeros([cnt, 3])
    # for i in range(2, cnt):
    #     data[i - 2] = lines[i].split(' ')
    # fin.close()
    numpy_arrays = np.array(data['point_set'])

    return numpy_arrays


def loadObj(fileName):
    fin = open(fileName, 'r')
    lines = fin.readlines()
    cnt = len(lines)
    print(cnt)
    # data = np.zeros([cnt, 3])
    for i in range(1, cnt):
        lines[i] = lines[i].strip('v ')
        # data[i-1] = lines[i].split(' ')
        if i == 1:
            # print(data[i-1])
            print(lines[i])
            break


def outputICP(fileName, data):
    file = '/home/du/iwaitPro/SketchPC/frontend/static/threeDs/'+fileName+'.obj'
    icp_file = '/home/du/iwaitPro/SketchPC/frontend/static/threeDs/icp_obj.obj'
    print('start output')
    print('output file name')
    print(file)
    print(icp_file)
    original = open(file, 'r')
    lines = original.readlines()
    cnt = len(lines)
    cnt2 = len(data)
    print('number')
    print(cnt)
    print(cnt2)
    fout = open(icp_file, "wb")
    i = 0
    for line in lines:
        if i < cnt2:
            line = 'v '+str(data[i][0]) + ' ' + \
                str(data[i][1]) + ' ' + str(data[i][2]) + '\n'
        i = i+1
        fout.write(line.encode())
    original.close()
    fout.close()
    return 'icp_obj'
