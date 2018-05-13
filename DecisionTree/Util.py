# -*- coding: utf-8 -*-

from Trees import *

def createDataSet():
    dataSet = [
            [1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']
            ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

def TestRun():
    myData, labels = createDataSet()
    #print calcShannonEntropy(myData)
    #print splitDataSet(myData, 0, 0)
    #print chooseBestFeatureToSplit(myData)
    
    print CreateTree(myData, labels)
    
TestRun()