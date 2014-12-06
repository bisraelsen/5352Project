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
        #print(pin[a])
        return pin[a]
    else:
        #print(pout[a])
        return pout[a]

def degV(v,block):
    deg_in = 0
    deg_out = 0
    #Loop through all vertices in the block
    for i in range(0,n[block]):
        if flip(pin[block]):
            deg_in += 1
    #loop through all vertices NOT of block
    for i in range(0,sum(np.array(n)[np.array(range(0,len(n)))!=block])):
        if flip(pout[block]):
            deg_out += 1
    #print(deg_in + deg_out)
    return deg_in + deg_out    
        
#Generate stochastic blockmodel graph    
#graph_tool.generation.random_graph(N, deg_sampler, directed=True, parallel_edges=False,
#     self_loops=False, block_membership=None, block_type='int', degree_block=False, random=True, verbose=False, **kwargs)


save_name = 'BM_n_' + str(N) + '_g_'+ str(len(n)) +  '.xml.gz'
g, bm = random_graph(N, degV, random=True, directed=False,n_iter=1000,
                         model="blockmodel",
                         block_membership=blockmembership,
                         vertex_corr=corr)

print(g.degree_property_map('total').a)
graph_draw(g,vertex_text=g.vertex_index, vertex_fill_color=bm, output="blockmodel_500.pdf")

g.set_directed(False)
    
g.save(save_name)
