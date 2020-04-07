#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/12/18 11:36
# @Author  : lxx
# @File    : process.py
# @Software: PyCharm
import os

attributeRootPath="D:\\LiuXianXian\\Pycharm--code\\WenDaYuLiaoSingleWord_timeAggregate\\timeData\\newAttribute"
instanceRootPath="D:\\LiuXianXian\\Pycharm--code\\WenDaYuLiaoSingleWord_timeAggregate\\timeData\\newInstance"

attributeFileList=os.listdir(attributeRootPath)
instanceFileList=os.listdir(instanceRootPath)
print(attributeFileList)
print(instanceFileList)

attributeAndInstanceDouble = []
for i in range(len(attributeFileList)):
    tmp = []
    tmp.append(instanceRootPath+"\\"+instanceFileList[i])
    tmp.append(attributeRootPath+"\\"+attributeFileList[i])
    attributeAndInstanceDouble.append(tmp)

print(attributeAndInstanceDouble)






replaceTime=[]

for time in open("replaceTime",encoding="utf-8"):
    time=time.strip()
    replaceTime.append(time)


with open("result.txt","w",encoding="utf-8") as resultFile:
    for tmpList in attributeAndInstanceDouble:
        print("开始。。。。。")
        instancePath=tmpList[0]
        attributePath=tmpList[1]
        replaceInstance=[]
        replaceAttribute=[]
        for instance in open(instancePath,encoding="utf-8"):
            instance=instance.strip()
            replaceInstance.append(instance)

        for attribute in open(attributePath,encoding="utf-8"):
            attribute=attribute.strip()
            replaceAttribute.append(attribute)


        for newInstance in replaceInstance:
            for newAttribute in replaceAttribute:
                for newTime in replaceTime:
                    if(newTime.startswith("####") or newTime == ""):
                        continue
                    tmpTime = newTime.split("###")
                    # if(tmpTime.__len__() != 2):
                    #     print(newTime)
                    for line in open("template.txt", encoding="utf-8"):
                        line = line.strip()
                        if(line.startswith("#")):
                            splitWords = line.split("|")
                            # print(splitWords)
                            # print(splitWords[10])

                            # if(splitWords.__len__() != 11):
                            #     print("=============================")
                            newLine = newInstance +"|"+ tmpTime[0] + "|" + splitWords[2] + "|" + tmpTime[1] + "|" + splitWords[4] + "|" + newAttribute +"|"+ splitWords[6] + "|" + splitWords[7] + "|" + splitWords[8] + "|" + splitWords[9] + "|" + splitWords[10]
                        elif(line.startswith("*")):
                            splitWords = line.split("|")
                            newLine = newInstance + "|" + tmpTime[0] + "|" + splitWords[2] + "|" + tmpTime[1] + "|" + \
                                      splitWords[
                                          4] + "|" + newAttribute + "|" + splitWords[6] + "|" + splitWords[7] + "|" + \
                                      splitWords[8]
                        elif(line.startswith("@")):
                            splitWords = line.split("|")
                            newLine = newInstance + "|" + splitWords[1] + "|" + tmpTime[0] + "|" + splitWords[3] + "|" + \
                                      tmpTime[1] + "|" + splitWords[5] + "|" + newAttribute + "|" + splitWords[7] + "|" + \
                                      splitWords[8] + "|" + splitWords[9]
                        elif(line.startswith("$")):
                            splitWords = line.split("|")
                            newLine =tmpTime[0] + "|" + splitWords[1] + "|" +tmpTime[1] + "|" +newInstance + "|" +splitWords[4] + "|" + \
                                     newAttribute + "|" + splitWords[6] + "|" + splitWords[7] + "|" + splitWords[8]
                        elif(line.startswith("%")):
                            splitWords = line.split("|")
                            newLine =newInstance + "|" +newAttribute + "|" + splitWords[2] + "|" +tmpTime[0] + "|" + \
                                     splitWords[4] + "|" +tmpTime[1] + "|" +splitWords[6] + "|" + splitWords[7] + "|" + splitWords[8]
                        else:
                            continue
                        resultFile.write(newLine)
                        resultFile.write("\n")

resultFile.close()
print("结束。。。。")
