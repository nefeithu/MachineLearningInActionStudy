# -*- coding: utf-8 -*-
from numpy import *
import operator
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
def classify0(inX, dataSet, labels, k):
    #1. 计算inx与 dataSet中每个点的距离
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    
    #2. 按照距离递增次序排序
    sortedDistIndices = distances.argsort()
    
    #3. 选取与当前点距离最小的K个点
    #4. 确定前K个点所在的类别的出现频率
    classCount = {}
    for i in range(k):
        label = labels[sortedDistIndices[i]]
        classCount[label] = classCount.get(label, 0) + 1
    
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse= True)
    
    #5. 返回出现频率最高的类别作为预测分类
    return sortedClassCount[0][0]

def file2Matrix(fileName):
    fr = open(fileName)
    arrayoLines = fr.readlines()
    numOfLine = len(arrayoLines)
    trainX = zeros((numOfLine, 3))
    trainY = []
    index = 0
    for line in arrayoLines:
        line = line.strip()
        listFromLine = line.split('\t')
        trainX[index, :] = listFromLine[0:3]
        trainY.append(int(listFromLine[-1]))
        index += 1
    return trainX, trainY

