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


def deg_sample():
    k = 3.0
    return k


g = random_graph(n,deg_sample,directed=False)

graph_draw(g)

fname = 'ER' + '_n_' + str(n) + '.xml.gz'

g.save(fname)
