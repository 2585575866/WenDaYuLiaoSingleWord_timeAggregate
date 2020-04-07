#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/12/18 11:36
# @Author  : lxx
# @File    : process.py
# @Software: PyCharm





print("开始。。。。。")
with open("result.txt","w",encoding="utf-8") as resultFile:
     for line in open("replaceAttribute_Value_Concept",encoding="utf-8"):
         line=line.strip()
         splitWords = line.split("\t")
         # print(splitWords)
         newAttribute=splitWords[0]
         newAttributeValue=splitWords[1]
         newConcept=splitWords[2]
         tmpAttribute=""
         tmpAttributeValue=""
         tmpConcept =""
         for singleStr in newAttribute:
             tmpAttribute=tmpAttribute+singleStr+" NN|"
         for singleStr in newConcept:
             tmpConcept = tmpConcept + singleStr + " NN|"
         for index,singleStr in enumerate(newAttributeValue):
             if(index ==0):
                 tmpAttributeValue = tmpAttributeValue + singleStr + " Bval|"
             elif(index==len(newAttributeValue) -1):
                 tmpAttributeValue = tmpAttributeValue + singleStr + " Eval|"
             else:
                 tmpAttributeValue = tmpAttributeValue + singleStr + " Mval|"
         for line1 in open("template.txt", encoding="utf-8"):
             line1 = line1.strip()
             # if (line.startswith("#")):


             split = line1.split("|")
             newLine = tmpAttribute  + split[1] + "|" + tmpAttributeValue  + split[3] + "|"+ tmpConcept  + split[5]+ "|"+ split[6]+ "|"+ split[7]
             resultFile.write(newLine)
             resultFile.write("\n")

print("结束。。。。")
