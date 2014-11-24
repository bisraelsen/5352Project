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
gName = g2f
if gName in glist:
    g = load_graph(gName)
else:
    g = collection.data[gName]
print("Processing " + gName)
#We are going to ignore anything outside the largest component
g = GraphView(g, vfilt=label_largest_component(GraphView(g, directed=False)))

state_MDL = minimize_blockmodel_dl(g)

b = state_MDL.b
k = len(set(b.a))
print("k = ", k)
state = BlockState(g, B=g.num_vertices(), deg_corr=True)
state = multilevel_minimize(state, B=k)
try:
    dirname = "MDL/" + gName.strip(".xml.gz")
    os.mkdir(dirname)
except:
    print("Directory already exists")

graph_draw(g,vertex_text=g.vertex_index,vertex_fill_color=state.get_blocks(), output=dirname+ "/" + gName.strip(".xml.gz") + ".pdf")
mat = state.get_matrix()
with open(dirname + "/mat.p","w") as outfile:
    pickle.dump(mat,outfile)
