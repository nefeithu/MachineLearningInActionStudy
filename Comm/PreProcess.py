# -*- coding: utf-8 -*-
from numpy import *

#归一化处理
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
