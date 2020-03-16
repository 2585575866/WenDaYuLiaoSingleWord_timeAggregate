#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/12/18 11:36
# @Author  : lxx
# @File    : process.py
# @Software: PyCharm



replaceLocal=[]
replaceConcept=[]


for local in open("replaceLocal_1",encoding="utf-8"):
    local=local.strip()
    replaceLocal.append(local)

for concept in open("replaceConcept_1",encoding="utf-8"):
    concept=concept.strip()
    replaceConcept.append(concept)



print("开始。。。。。")
with open("result_1.txt","w",encoding="utf-8") as resultFile:
    for newLocal in replaceLocal:
        for newConcept in replaceConcept:
                # print(tmpTime)
                for line in open("template.txt",encoding="utf-8"):
                    line=line.strip()
                    splitWords = line.split("|")
                    # print(splitWords)
                    tmpLocal=""
                    tmpConcept=""
                    for index,singleStr in enumerate(newLocal):
                        if(index == 0):
                            tmpLocal = tmpLocal + singleStr + " Bgloc|"
                        elif(index == len(newLocal)-1):
                            tmpLocal = tmpLocal + singleStr + " Egloc|"
                        else:
                            tmpLocal = tmpLocal + singleStr + " Mgloc|"

                    for singleStr in newConcept:
                        tmpConcept = tmpConcept+singleStr + " NN|"

                    newLine = splitWords[0] + "|"+ splitWords[1] + "|" + splitWords[2] + "|" +splitWords[3] + "|"+tmpLocal+ splitWords[5] + "|"+ splitWords[6] + "|" + splitWords[7]+"|"+tmpConcept
                    newLine=newLine[0:-1]
                    resultFile.write(newLine)
                    resultFile.write("\n")

print("结束。。。。")
