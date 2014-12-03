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

n = 1000
lam =5 

def deg_sample():
   return np.random.poisson(lam)

g = random_graph(n,deg_sample,directed=False)

graph_draw(g)

fname = 'Poisson' + '_n_' + str(n)+ '_lam_'+ str(lam) + '.xml.gz'

g.save(fname)
