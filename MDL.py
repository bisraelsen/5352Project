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

gList = [g1f,g2f,g3f,g4f,g5f]

g1 = load_graph(gList[4])

g = collection.data["serengeti-foodweb"]

state = minimize_blockmodel_dl(g)

b = state.b
#t = get_hierarchy_tree(bstack)
print(len(set(b.a)))
graph_draw(g,vertex_fill_color=b)

print('here')