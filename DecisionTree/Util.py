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

def RetrieveTree(i):
    trees = [
            {'no surfacing': {0:'no', 1: {'flippers':\
                                          {0:'no', 1:'yes'}}}},
            {'no surfacing':{0:'no', 1:{'flippers':\
                                        {0:{'head':{0:'no', 1:'yes'}}, 1:'no'}}}}
            ]
    return trees[i]

def TestRun():
    myData, labels = createDataSet()
    #print calcShannonEntropy(myData)
    #print splitDataSet(myData, 0, 0)
    #print chooseBestFeatureToSplit(myData)
    
    myTree = RetrieveTree(0)
    print myTree
    print Classify(myTree, labels, [1,0])
    print Classify(myTree, labels, [1,1])
    
TestRun()