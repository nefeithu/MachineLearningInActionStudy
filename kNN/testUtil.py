# -*- coding: utf-8 -*-
"""
Created on Sun May 06 17:11:37 2018

@author: xiaoqhu
"""
from kNN import *
from Comm.PreProcess import autoNorm
def createDataSet():
    group= array([[1.0, 1.1],[1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


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
        predict = classify0(normData[i, :], normData[numTest:m, :], datingLables[numTest:m], 3)
        print "predict %d, real is %d" %(predict, datingLables[i])
        if predict != datingLables[i]:
            errCnt += 1.0
    print "err cnt= %f, testCnt=%d, err percent=%f" %(errCnt, numTest, errCnt/numTest)
            
    


#mySimpleTest()
datingClassTest()
