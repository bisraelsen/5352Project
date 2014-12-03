import scipy.io 
import scipy.misc
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
import pickle
from graph_tool.all import *
#import subprocess
import sys
#import StringIO
import time
import os
from random import randint, sample, random
#from mercurial.demandimport import nothing
from datetime import datetime

g1f = 'bowtie.xml.gz'
g2f = 'karate_club_edges.xml.gz'
g3f = 'RLT_c_4_g_30.xml.gz'
g4f = 'RLT_c_40_g_3.xml.gz'
g5f = 'RLT_c_40_g_30.xml.gz'
glist = [g1f,g2f,g3f,g4f,g5f]

maxB = {}
for (gName,g) in ([(x,load_graph(x)) for x in glist] + collection.data.items()):
    
    print("Processing " + gName)
    #We are going to ignore anything outside the largest component
    g = GraphView(g, vfilt=label_largest_component(GraphView(g, directed=False)))
    print("N = " + str(g.num_vertices()) + "E = " + str(g.num_edges()))
    maxB[gName] = get_max_B(N=g.num_vertices(),E=g.num_edges())
    print("max b for " + gName + " is " + str(maxB[gName]))

pickle.dump(maxB,open( "maxB.p", "wb" ))
