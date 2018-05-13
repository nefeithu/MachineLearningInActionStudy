# -*- coding: utf-8 -*-
from math import log
import operator

def CreateTree(dataSet, labels):
    #如果dataSet都是同一个类别，则直接返回
    typeCnt = [x[-1]  for x  in dataSet]
    if typeCnt.count(typeCnt[0]) == len(typeCnt):
        return typeCnt[0]
    #如果只剩一个特征，直接返回
    if len(dataSet[0]) == 1:
        return majorCnt(typeCnt)
    
    bestFeaIdx = chooseBestFeatureToSplit(dataSet)
    bestLabel = labels[bestFeaIdx]
    
    myTree = {bestLabel: {}}
    del(labels[bestFeaIdx])
    
    feaList = [x[bestFeaIdx] for x in dataSet]
    uniqueFeaList = set(feaList)
    
    for x in uniqueFeaList:
        subLabels = labels[:]
        myTree[bestLabel][x] = CreateTree(splitDataSet(dataSet, bestFeaIdx, x), subLabels)  
    
    return myTree

def calcShannonEntropy(dataSet):
    nNum = len(dataSet)
    labelStatics = {}
    
    #统计各个类别的样本数
    for x in dataSet:
        label = x[-1]
        if label not in labelStatics.keys():
            labelStatics[label] = 0
        labelStatics[label] += 1
        
    #计算ShannonEntropy
    shEnt = 0.0
    for key in labelStatics:
        prob = float(labelStatics[key])/nNum
        shEnt -= prob * log(prob, 2)
    
    return shEnt

#根据指定索引特征的指定值来划分抽取数据子集
def splitDataSet(dataSet, xIdx, xValue):
    retDataSet = []
    for x in dataSet:
        if x[xIdx] == xValue:
            newX = x[:xIdx]
            newX.extend(x[xIdx + 1 : ])
            retDataSet.append(newX)
    return retDataSet

#选取最好的数据划分方式
def chooseBestFeatureToSplit(dataSet):
    fDims = len(dataSet[0]) - 1
    baseEnt = calcShannonEntropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(fDims):
        flist = [x[i] for x in dataSet]
        uniqueVar = set(flist)
        sumEnt = 0.0
        for j in uniqueVar:
            retDataSet = splitDataSet(dataSet, i, j)
            ratio = float(len(retDataSet))/len(dataSet)
            sumEnt += ratio * calcShannonEntropy(retDataSet)
        tmpInfoGain = baseEnt - sumEnt
        if (tmpInfoGain > bestInfoGain):
            bestInfoGain = tmpInfoGain
            bestFeature = i
    return bestFeature

def majorCnt(classList):
    labelCnt = {}
    for x in classList:
        if x not in labelCnt.keys():
            labelCnt[x] = 0
        labelCnt[x] += 1
    sorted(labelCnt.iteritems(), operator.itemgetter(1), reverse = True)
    return  labelCnt[0][0]