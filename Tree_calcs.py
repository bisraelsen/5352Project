#!/usr/bin/env python

from pylab import savefig
from vbmod import *
import matplotlib.pyplot as plt
import pickle

from graph_tool.all import *
import os
import sys

graph_loc = "~/brett.israelsen@gmail.com/Education/Graduate/Fall 2014/CS5352/Project/saved_graphs"

files = os.listdir(graph_loc)

n_pct_dist_b = {}
lvl_dist_b = {}

n_pct_dist_m = {}
lvl_dist_m = {}

for f in files[1:2]:
    if "Tree" in f:
        g = load_graph(f)
        n = g.num_vertices()    
        b_grp = g.vp['bayes'].a
        m_grp = g.vp['mdl'].a

        lvls = g.vp['Level'].a

        for grp in list(set(b_grp)):
            lvl_dist_b[f].append(lvls[b_grp == grp])
            n_pct_dist_b[f].append(sum(b_grp == grp)/n)

        for grp in list(set(m_grp)):
            lvl_dist_m[f].append(lvls[m_grp == grp])
            n_pct_dist_m[f].append(sum(m_grp == grp)/n)






        
