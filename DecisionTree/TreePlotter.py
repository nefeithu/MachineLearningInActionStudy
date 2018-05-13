# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def CreatePlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    CreatePlot.ax1 = plt.subplot(111, frameon=False)
    PlotNode('DecisionNode', (0.5, 0.1), (0.1, 0.5), decisionNode)
    PlotNode('LeafNode', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()
    
def PlotNode(nodeTxt, centerPoint, parentPoint, NodeType):
    CreatePlot.ax1.annotate(nodeTxt, xy=parentPoint, \
                            xycoords='axes fraction',\
                            xytext=centerPoint,\
                            textcoords='axes fraction',\
                            va="center", ha="center", bbox=NodeType,\
                            arrowprops=arrow_args
            )


CreatePlot()
