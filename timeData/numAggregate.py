#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/3/8 18:44
# @Author  : lxx
# @File    : numAggregate.py
# @Software: PyCharm
import os
import re


attributeRootPath="D:\\LiuXianXian\\Pycharm--code\\WenDaYuLiaoSingleWord_timeAggregate\\timeData\\Attribute"
instanceRootPath="D:\\LiuXianXian\\Pycharm--code\\WenDaYuLiaoSingleWord_timeAggregate\\timeData\\Instance"

newAttributeRootPath="D:\\LiuXianXian\\Pycharm--code\\WenDaYuLiaoSingleWord_timeAggregate\\timeData\\newAttribute"
newInstanceRootPath="D:\\LiuXianXian\\Pycharm--code\\WenDaYuLiaoSingleWord_timeAggregate\\timeData\\newInstance"


instanceFileList=os.listdir(instanceRootPath)
attributeFileList=os.listdir(attributeRootPath)



instancePaths=[]
attributePaths = []
newInstancePaths=[]
newAttributePaths = []
for i in range(len(instanceFileList)):
    instancePaths.append(instanceRootPath+"\\"+instanceFileList[i])
    newInstancePaths.append(newInstanceRootPath+"\\"+"new"+instanceFileList[i])
for i in range(len(attributeFileList)):
    attributePaths.append(attributeRootPath+"\\"+attributeFileList[i])
    newAttributePaths.append(newAttributeRootPath+"\\"+"new"+attributeFileList[i])



for index,instancePath in enumerate(instancePaths):
    # print(instancePath)
    with open(newInstancePaths[index],"w",encoding="utf-8") as newFile:
        for line in open(instancePath,encoding="utf-8"):
            line=line.strip()
            # print(line)
            newLine=""
            if (line != ""):
                # lists = re.split("([\u4e00-\u9fff])", line)
                lists = re.split("([a-zA-Z]+|[\u4e00-\u9fff])", line)
                # print(lists)
                for li in lists:
                    if(li !=""):
                        newLine=newLine+li+" NN|"
            newFile.write(newLine[:-1])
            newFile.write("\n")


for index,attributePath in enumerate(attributePaths):
    # print(instancePath)
    with open(newAttributePaths[index],"w",encoding="utf-8") as newFile:
        for line in open(attributePath,encoding="utf-8"):
            line=line.strip()
            # print(line)
            newLine=""
            if (line != ""):
                lists = re.split("([\u4e00-\u9fff])", line)
                # print(lists)
                for li in lists:
                    if(li !=""):
                        newLine=newLine+li+" NN|"
            newFile.write(newLine[:-1])
            newFile.write("\n")












