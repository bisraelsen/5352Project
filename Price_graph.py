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
c1 = 4 


g = price_network(n,m=c1)
g.set_directed(False)
graph_draw(g)

fname = 'Prices' + '_n_' + str(n)+ '_m_'+ str(c1) + '.xml.gz'

g.save(fname)
