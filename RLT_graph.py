import scipy.io 
import scipy.misc
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
from graph_tool.all import *
import random
import sys
import time
import os

cliqueSize = 16
numCliques = 2

g = Graph()
g.set_directed(False)
grp = g.new_vertex_property('int')
g.vp['Group'] = grp

def makeClique(g,size,grp_num):    
    
    g2 = complete_graph(size)
    
    grp = g2.new_vertex_property('int')
    grp.a = grp_num
    g2.vp['Group'] = grp
    
    graph_union(g, g2,props=[(g.vp['Group'], g2.vp['Group'])], include=True)
    
    return g
        
def connectCliques(g,grpString):
    grpList = list(set(g.vp[grpString].a))
    
    vBridges = []
    for i in grpList:
        g2 = GraphView(g,vfilt=lambda v: g.vp[grpString][v] == i)
        vBridges.append(random.choice(list(g2.vertices())))
    
    lstvBridges = list(vBridges)
    
    for i in range(0,len(lstvBridges)):
        if len(lstvBridges) == 2:
            g.add_edge(lstvBridges[i],lstvBridges[1])
            break
        else:
            if i != len(lstvBridges)-1:
                g.add_edge(lstvBridges[i],lstvBridges[i+1])
            else:
                g.add_edge(lstvBridges[i],lstvBridges[0])

for i in range(0,numCliques):
    g = makeClique(g,cliqueSize,i)

connectCliques(g,'Group')
    

graph_draw(g,vertex_fill_color = g.vp['Group'])

fname = 'RLT_c_' + str(cliqueSize) + '_g_' + str(numCliques) + '.xml.gz'

g.save(fname)
