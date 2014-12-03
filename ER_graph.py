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
k = 5.0

def deg_sample():
    return k


g = random_graph(n,deg_sample,directed=False)

graph_draw(g)

fname = 'ER' + '_n_' + str(n)+ '_k_'+ str(k) + '.xml.gz'

g.save(fname)
