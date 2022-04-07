# import os

# rootDir = '/media/du/DATA/finalData'

# for lists in os.listdir(rootDir):
#     path = os.path.join(rootDir, lists)
#     print(path)
#     if os.path.isdir(path):
#     for subLists in os.listdir(path):
#         subPath = os.path.join(path, subLists)
#         print(subPath)

import os
import shutil

rootdir = "/media/du/DATA/finalData"
# writePath = open('/home/du/writepath.txt', 'w')
destPath = "/media/du/DATA/finalDataObject"
# 获取目录下文件名清单
list = os.listdir(rootdir)
# print(list)

# #移动图片到指定文件夹
# 遍历目录下的所有文件夹
for i in range(0, len(list)):
    path = os.path.join(rootdir, list[i])
    # print(path)
    if os.path.isdir(path):  # 判断是否为文件夹
        subList = os.listdir(path)
        for j in range(0, len(subList)):
            subPath = os.path.join(path, subList[j])
            # print(subPath)
            if os.path.isdir(subPath):
                subsubList = os.listdir(subPath)
                for k in range(0, len(subsubList)):
                    type = os.path.splitext(subsubList[k])[1]
                    if type == '.obj':
                        subsubPath = os.path.join(subPath, subsubList[k])
                        shutil.copy(subsubPath, destPath)

                        # newName = list[i]+'_'+subList[j]+'_'+subsubList[k]
                        # newsubsubPath = os.path.join(subPath, newName)
                        # os.rename(subsubPath, newsubsubPath)
                        # writePath.write(subsubPath+'\n')
                        # writePath.write(newsubsubPath+'\n')
                        # print(type)
                        # writePath.write(type)
# writePath.close()

# for item in os.listdir(path):  # 遍历该文件夹中的所有文件
#     # 将根目录与文件夹名连接起来，获取文件目录
#     dirname = os.path.join(
#         "E:/BaiduNetdiskDownload/jaffedbase/resize128_out", list[i])
#     full_path = os.path.join(dirname, item)  # 将文件目录与文件名连接起来，形成原来完整路径
#     des_path = "E:/BaiduNetdiskDownload/jaffedbase/resize128_out/1.image"  # 目标路径
#     shutil.move(full_path, des_path)  # 移动文件到目标路径
#     print(full_path)
#     print(des_path)
