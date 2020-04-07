#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/12/18 11:36
# @Author  : lxx
# @File    : process.py
# @Software: PyCharm



replaceLocal=[]
replaceConcept=[]


for local in open("replaceLocal_2",encoding="utf-8"):
    local=local.strip()
    replaceLocal.append(local)

for concept in open("replaceConcept_2",encoding="utf-8"):
    concept=concept.strip()
    replaceConcept.append(concept)



print("开始。。。。。")
with open("result_2.txt","w",encoding="utf-8") as resultFile:
    for newLocal in replaceLocal:
        if (len(newLocal) == 0):
            break
        for newConcept in replaceConcept:
                # print(tmpTime)
                for line in open("template.txt",encoding="utf-8"):
                    line=line.strip()
                    splitWords = line.split("|")
                    # print(splitWords)
                    tmpLocal=""
                    # tmpConcept=""
                    if(len(newLocal)==1):
                        tmpLocal = " Sdloc|"
                    if(len(newLocal) > 1):
                        for index,singleStr in enumerate(newLocal):
                            if(index == 0):
                                tmpLocal = tmpLocal + singleStr + " Bdloc|"
                            elif(index == len(newLocal)-1):
                                tmpLocal = tmpLocal + singleStr + " Edloc|"
                            else:
                                tmpLocal = tmpLocal + singleStr + " Mdloc|"

                    # for singleStr in newConcept:
                    #     tmpConcept = tmpConcept+singleStr + " NN|"

                    newLine = tmpLocal  + splitWords[1] + "|" +newConcept+" NN|"
                    newLine=newLine[0:-1]
                    resultFile.write(newLine)
                    resultFile.write("\n")

print("结束。。。。")
