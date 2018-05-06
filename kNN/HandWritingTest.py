# -*- coding: utf-8 -*-
"""
Created on Sun May 06 22:10:41 2018

@author: xiaoqhu
"""
from kNN import *
from os import listdir

# file: 32*32
def img2vector(filename):
    ret = zeros((1, 1024))
    f = open(filename)
    for i in range(32):
        line = f.readline()
        for j in range(32):
            ret[0][i * 32 + j] = int(line[j])
    
    return ret

def mudTest():
    testVec = img2vector('testDigits/0_13.txt')
    print testVec[0, 0:31]
    print testVec[0, 32:63]
    
def handwritingClassTest():
    trainY = []
    trainFiles = listdir('trainingDigits')
    m = len(trainFiles)
    trainX = zeros((m, 1024))
    
    for i in range(m):
        fileName = trainFiles[i]
        fileStr = fileName.split('.')[0]
        classNum = int(fileStr.split('_')[0])
        trainY.append(classNum)
        trainX[i, :] = img2vector('trainingDigits/%s' % fileName)
    
    testFiles = listdir('testDigits')
    errCnt = 0
    mTest = len(testFiles)
    
    for i in range(mTest):
        fileName = testFiles[i]
        fileStr = fileName.split('.')[0]
        classNum = int(fileStr.split('_')[0])
        testVec = img2vector('testDigits/%s' % fileName)
        
        predict = classify0(testVec, trainX, trainY, 3)
        
        if classNum != predict:
            errCnt += 1
            print "predict to be %d, the real label is %d, testFileName %s" %(predict, classNum, fileName)
    print "total test %d, err cnt %d, err rate %f" %(mTest, errCnt, float(errCnt)/mTest)
        
        #print fileName
    
handwritingClassTest()