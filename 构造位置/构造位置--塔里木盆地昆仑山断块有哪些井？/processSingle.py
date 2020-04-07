#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/12/18 11:36
# @Author  : lxx
# @File    : process.py
# @Software: PyCharm



replaceLocal=[]
replaceConcept=[]
replaceMethod=[]


for local in open("replaceLocal_1",encoding="utf-8"):
    local=local.strip()
    replaceLocal.append(local)

for concept in open("replaceConcept_1",encoding="utf-8"):
    concept=concept.strip()
    replaceConcept.append(concept)

for method in open("replaceMethod",encoding="utf-8"):
    method=method.strip()
    replaceMethod.append(method)



print("开始。。。。。")
with open("result_1.txt","w",encoding="utf-8") as resultFile:
    for newLocal in replaceLocal:
        if (len(newLocal) == 0):
            break
        for newConcept in replaceConcept:
                # print(tmpTime)
                tmpLocal = ""
                tmpConcept = ""
                if (len(newLocal) == 1):
                    tmpLocal = " Sgloc|"
                if (len(newLocal) > 1):
                    for index, singleStr in enumerate(newLocal):
                        if (index == 0):
                            tmpLocal = tmpLocal + singleStr + " Bgloc|"
                        elif (index == len(newLocal) - 1):
                            tmpLocal = tmpLocal + singleStr + " Egloc|"
                        else:
                            tmpLocal = tmpLocal + singleStr + " Mgloc|"

                for singleStr in newConcept:
                    tmpConcept = tmpConcept + singleStr + " NN|"

                for newMethod in replaceMethod:
                    tmpMethod=""
                    for singleMethod in newMethod:
                        tmpMethod = tmpMethod + singleMethod + " NN|"

                    for line in open("template.txt",encoding="utf-8"):
                        line=line.strip()
                        splitWords = line.split("|")
                        newLine=""
                        #一组 有哪些 井筒
                        if(line.startswith("1")):
                            newLine = tmpLocal  + tmpMethod  +tmpConcept
                            newLine=newLine[0:-1]
                        #一组 有那些 口 井筒
                        elif (line.startswith("2")):
                            newLine = tmpLocal + tmpMethod  + splitWords[2] + "|"  + tmpConcept
                            newLine = newLine[0:-1]
                        #一组 的 井筒 有多少
                        elif (line.startswith("3")):
                            newLine = tmpLocal + splitWords[1] + "|" +tmpConcept +tmpMethod
                            newLine = newLine[0:-1]
                        #一组 的 井筒 有多少 口
                        elif (line.startswith("4")):
                            newLine = tmpLocal + splitWords[1] + "|" + tmpConcept + tmpMethod +splitWords[4]
                            # newLine = newLine[0:-1]
                        #一组 有哪些 井筒 ?
                        elif (line.startswith("5")):
                            newLine = tmpLocal +tmpMethod + tmpConcept + splitWords[3]
                            # newLine = newLine[0:-1]
                        #一组 有多少 口 井筒 ?
                        elif (line.startswith("6")):
                            newLine = tmpLocal + tmpMethod +splitWords[2] + "|" + tmpConcept+ splitWords[4]
                            # newLine = newLine[0:-1]
                        #一组 的 井筒 有哪些 ?
                        elif (line.startswith("7")):
                            newLine = tmpLocal + splitWords[1] + "|" + tmpConcept + tmpMethod + splitWords[4]
                            # newLine = newLine[0:-1]
                        #一组 的 井筒 有多少 口 ?
                        elif (line.startswith("8")):
                            newLine = tmpLocal + splitWords[1] + "|" + tmpConcept + tmpMethod + splitWords[4] + "|" +splitWords[5]
                            # newLine = newLine[0:-1]
                        #地 理 位 置 一组 有哪些 井筒
                        elif (line.startswith("9")):
                            # print("999999")
                            newLine = splitWords[0][1:]+ "|"+splitWords[1]+"|"+splitWords[2]+"|"+splitWords[3]+ "|"+tmpLocal +tmpMethod + tmpConcept
                            newLine = newLine[0:-1]
                        #地 理 位 置 一组 有多少 口 井筒
                        elif (line.startswith("a")):

                            newLine = splitWords[0][1:]+ "|"+splitWords[1]+"|"+splitWords[2]+"|"+splitWords[3] + "|" + tmpLocal + tmpMethod+ splitWords[6] + "|" + tmpConcept
                            newLine = newLine[0:-1]
                        #地 理 位 置 是 一组 的 有哪些 井筒
                        elif (line.startswith("b")):

                            newLine = splitWords[0][1:]+ "|"+splitWords[1]+"|"+splitWords[2]+"|"+splitWords[3] + "|" + splitWords[4] + "|"+ tmpLocal + splitWords[6] + "|" + tmpMethod + tmpConcept
                            newLine = newLine[0:-1]
                        #地 理 位 置 是 一组 的 有多少 口 井筒
                        elif (line.startswith("c")):
                            newLine = splitWords[0][1:]+ "|"+splitWords[1]+"|"+splitWords[2]+"|"+splitWords[3] + "|" + splitWords[4] + "|" + tmpLocal + splitWords[6] + "|" + \
                                      tmpMethod + "|" +splitWords[8] + "|"+ tmpConcept
                            newLine = newLine[0:-1]
                        #地理位置 是 一组 的 井筒 有哪些
                        elif (line.startswith("d")):
                            newLine = splitWords[0][1:]+ "|"+splitWords[1]+"|"+splitWords[2]+"|"+splitWords[3] + "|" + splitWords[4] + "|" + tmpLocal + splitWords[6] + "|" + \
                                      tmpConcept+tmpMethod
                            newLine = newLine[0:-1]
                        #地 理 位 置 是 一组 的 井筒 有多少 口
                        elif (line.startswith("e")):
                            newLine = splitWords[0][1:] + "|" + splitWords[1] + "|" + splitWords[2] + "|" + \
                                      splitWords[3] + "|" + splitWords[4] + "|" + tmpLocal + splitWords[6] + "|" + \
                                      tmpConcept+tmpMethod+ splitWords[9]
                            # newLine = newLine[0:-1]
                        #地 理 位 置 一组 有哪些 井筒 ？
                        elif (line.startswith("f")):
                            newLine = splitWords[0][1:] + "|" + splitWords[1] + "|" + splitWords[2] + "|" + \
                                      splitWords[3] + "|"+ tmpLocal +  tmpMethod+ \
                                      tmpConcept +   splitWords[7]
                            # newLine = newLine[0:-1]
                        #地 理 位 置 一组 有哪些 口 井筒 ？
                        elif (line.startswith("g")):
                            newLine = splitWords[0][1:] + "|" + splitWords[1] + "|" + splitWords[2] + "|" + \
                                      splitWords[3] + "|" + tmpLocal + tmpMethod +tmpConcept + splitWords[8]
                            # newLine = newLine[0:-1]
                        #地 理 位 置 是 一组 的 有哪些 井筒 ？
                        elif (line.startswith("h")):
                            newLine = splitWords[0][1:] + "|" + splitWords[1] + "|" + splitWords[2] + "|" + \
                                      splitWords[3] + "|" + splitWords[4] + "|" +tmpLocal +splitWords[6] + "|" + tmpMethod  \
                                      + tmpConcept+splitWords[9]
                            # newLine = newLine[0:-1]
                        #地 理 位 置 是 一组 的 有哪些 口 井筒 ？
                        elif (line.startswith("i")):
                            newLine = splitWords[0][1:] + "|" + splitWords[1] + "|" + splitWords[2] + "|" + \
                                      splitWords[3] + "|" + splitWords[4] + "|" + tmpLocal + splitWords[6] + "|" + tmpMethod +splitWords[8] + "|" + tmpConcept+splitWords[10]
                            # newLine = newLine[0:-1]
                        #地 理 位 置 是 一组 的 井筒 有哪些 ？
                        elif (line.startswith("j")):
                            newLine = splitWords[0][1:] + "|" + splitWords[1] + "|" + splitWords[2] + "|" + \
                                      splitWords[3] + "|" + splitWords[4] + "|" + tmpLocal + splitWords[6] + "|" + tmpConcept+tmpMethod +splitWords[9]
                            # newLine = newLine[0:-1]
                        #地 理 位 置 是 一组 的 井筒 有哪些 口 ？
                        elif (line.startswith("k")):
                            newLine = splitWords[0][1:] + "|" + splitWords[1] + "|" + splitWords[2] + "|" + \
                                      splitWords[3] + "|" + splitWords[4] + "|" + tmpLocal + splitWords[6] + "|" + tmpConcept + tmpMethod+splitWords[9] + "|" + splitWords[10]
                            # newLine = newLine[0:-1]
                        if(newLine !=""):

                            resultFile.write(newLine)
                            resultFile.write("\n")

print("结束。。。。")
