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

levels = 5 
children = 10

g = Graph()
g.set_directed(False)

#Add initial "seed" vertex
g.add_vertex()

#assign level to the first vertex
v = g.vertex(0)
lvl = g.new_vertex_property('int')
lvl[v] = 0
g.vp['Level'] = lvl


def makeLevel(g,lvlString):    
    lvlList = list(set(g.vp[lvlString].a))
    nxtLevel = max(lvlList)+1
    
    g2 = GraphView(g,vfilt=lambda v: g.vp[lvlString][v] == nxtLevel-1)
    numVs = g2.num_vertices()

    g3 = Graph()
    g3.add_vertex(numVs*children)

    lvl_prop = g3.new_vertex_property('int')
    lvl_prop.a = nxtLevel
    g3.vp[lvlString]=lvl_prop
      
    graph_union(g, g3,props=[(g.vp[lvlString], g3.vp[lvlString])], include=True)
    
    return g

def connectLevels(g,lvlString):
    grpList = list(set(g.vp[lvlString].a))
    
    lvlList = []
    for i in grpList:
        g2 = GraphView(g,vfilt=lambda v: g.vp[lvlString][v] == i)
        lvlList.append(list(g2.vertices()))
    
    for i in range(0,len(lvlList)-1):
        edge_count = 0
        for j in range(0,len(lvlList[i])):
            for k in range(0,children):
                g.add_edge(lvlList[i][j],lvlList[i+1][edge_count])
                edge_count += 1

#start at 1 because 0 has already been added
for i in range(1,levels):
    g = makeLevel(g,'Level')

connectLevels(g,'Level')

graph_draw(g)

fname = 'Tree' + '_c_' + str(children)+ '_l_'+ str(levels) + '.xml.gz'

g.save(fname)
