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
name = 'polbooks'

g = collection.data[name]
random_rewire(g,model = 'uncorrelated')

graph_draw(g)

fname = 'CFG_' + name + '.xml.gz'

g.save(fname)
