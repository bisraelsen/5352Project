import scipy.io 
import scipy.misc
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
#import pickle
from graph_tool.all import *
#import subprocess
import sys
#import StringIO
import os
from random import randint, sample, random

#Define SBM Properties
pin = [float(x) for x in sys.argv[1].split(',')]
pout = [float(x) for x in sys.argv[2].split(',')]

n = [int(x) for x in sys.argv[3].split(',')]
N = sum(n)

blockmembership = []
for i in range(0,len(n)):
    blockmembership = blockmembership + [i] * n[i]

def flip(p):
    return 1 if random() < p else 0

#Function defining the probabilities that differentg groups will connect to eachother
def corr(a, b):
    if a == b:
        return pin[a]
    else:
        return pout[a]

def degV(v,block):
    deg = 0
    for i in range(0,n[block]):
        if flip(pin[block]):
            deg += 1
    for i in range(0,sum(np.array(n)[np.array(range(0,len(n)))!=block])):
        if flip(pin[block]):
            deg += 1
    #print(deg)
    return deg    
        
#Generate stochastic blockmodel graph    
#graph_tool.generation.random_graph(N, deg_sampler, directed=True, parallel_edges=False,
#     self_loops=False, block_membership=None, block_type='int', degree_block=False, random=True, verbose=False, **kwargs)


save_name = 'BM_n_' + str(N) + '_g_'+ str(len(n)) +  '.xml.gz'
g, bm = random_graph(N, degV, directed=False,
                         model="blockmodel-traditional",
                         block_membership=blockmembership,
                         vertex_corr=corr)

graph_draw(g, vertex_fill_color=bm, edge_color="black", output="blockmodel_500.pdf")

g.set_directed(False)
    
g.save(save_name)
