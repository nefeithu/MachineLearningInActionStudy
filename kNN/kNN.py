# -*- coding: utf-8 -*-
from numpy import *
import operator
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
def createDataSet():
    group= array([[1.0, 1.1],[1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

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

def autoNorm(dataSet):
    #参数0使得从列中选取最小、最大值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = dataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

def mySimpleTest():
#    trainX, trainY = createDataSet()
#    testX = array([[0.5, 0.4]])
#    predict = classify0(testX, trainX, trainY, 3)
#    print 'predict=', predict
    
    #load data
    datingX, datingY = file2Matrix('datingTestSet2.txt')
#    print datingX, datingY
    #myDisplay(datingX, datingY)
    normMat, ranges, minVals = autoNorm(datingX)
    print normMat
    print ranges

def myDisplay(datingX, datingY):
    import matplotlib
    import matplotlib.pyplot as plt
    
    type_1_x = []
    type_1_y = []
    type_2_x = []
    type_2_y = []
    type_3_x = []
    type_3_y = []
    for i in range(len(datingX)):
        if datingY[i] == 1:
            type_1_x.append(datingX[i][0])
            type_1_y.append(datingX[i][1])
        elif datingY[i] == 2:
            type_2_x.append(datingX[i][0])
            type_2_y.append(datingX[i][1])
        elif datingY[i] == 3:
            type_3_x.append(datingX[i][0])
            type_3_y.append(datingX[i][1])
        else:
            print datingY[i], type(datingY[i])
            
    fig = plt.figure()
    axes = plt.subplot(111)  
    plt.xlabel('fly time')
    plt.ylabel('game time')
    plt.scatter(type_1_x, type_1_y, s=20, c='r', label='not like')   
    axes.scatter(type_2_x, type_2_y, s=40, c='b', label='yiban')   
    axes.scatter(type_3_x, type_3_y, s=60, c='g', label='verylike')  
    plt.grid()
    plt.legend()
    #plt.legend((type1, type2, type3), ('not like', 'yiban', 'very like'))
    plt.show()
    
def  datingClassTest():
    testRation = 0.1
    datingData, datingLables = file2Matrix('datingTestSet2.txt')
    normData, ranges, minVals = autoNorm(datingData)
    m = normData.shape[0]
    numTest = int(m * testRation)
    errCnt = 0
    for i in range(numTest):
        predict = classify0(normData[i, :], normData[numTest:m, :], datingLables[numTest:m, :], 3)
        print "predict %d, real is %d" %(predict, datingLables[i])
        if predict != datingLables[i]:
            errCnt += 1.0
    print "err cnt= %f, testCnt=%d, err percent=%f" %(errCnt, numTest, errCnt/numTest)
            
    


#mySimpleTest()
datingClassTest()

