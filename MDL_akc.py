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
#to calculate the <k> to detect the true partition
g1f = 'bowtie.xml.gz'
g2f = 'karate_club_edges.xml.gz'
glist = [g1f,g2f]
groupNames = ['goodGroup','Social']
cnt = 0
akc = {}
for (gName,g) in ([(x,load_graph(x)) for x in glist]):
    
    print("Processing " + gName)
    #We are going to ignore anything outside the largest component
    g = GraphView(g, vfilt=label_largest_component(GraphView(g, directed=False)))
    B = len(set(g.vp[groupNames[cnt]].a))
    get_akc(2,(2.0*(1.0/14.0)*np.log((1.0/14.0)/(0.25)))/(2.0*(1.0/14.0)*np.log((1.0/14.0)/(.8571))),N=6)
    akc[gName] = get_akc(B,)
    print("max b for " + gName + " is " + str(maxB[gName]))
    cnt += 1
pickle.dump(maxB,open( "maxB.p", "wb" ))
