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
                    # print(tmpTime)
                    for line in open("template.txt",encoding="utf-8"):
                        line=line.strip()
                        if(line.startswith("#")):
                            splitWords = line.split("|")
                            newLine = newInstance+"|"  + newTime + "|" + splitWords[2] + "|" + newAttribute +"|" + splitWords[4]+ "|"+ splitWords[5]+ "|"+ splitWords[6]
                        elif(line.startswith("*")):
                            splitWords = line.split("|")
                            newLine = newTime + "|" + newInstance + "|" + splitWords[2] + "|" + newAttribute + "|" + \
                                      splitWords[4] + "|" + splitWords[5] + "|" + splitWords[6]

                        resultFile.write(newLine)
                        resultFile.write("\n")

resultFile.close()
print("结束。。。。")
