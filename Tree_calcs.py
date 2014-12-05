#!/usr/bin/env python

from vbmod import *
import matplotlib.pyplot as plt
from graph_tool.all import *
import numpy as np
import sys
import scipy

#graph_loc = sys.argv[1]
graph_loc = "/home/brett/brett.israelsen@gmail.com/Education/Graduate/Fall 2014/CS5352/Project/saved_graphs/Tree_c_2_l_10.g.xml.gz"
g = load_graph(graph_loc)
N = g.num_vertices()

b_grp = g.vp['bayes'].a
m_grp = g.vp['mdl'].a
l_grp = g.vp['Level'].a
print(b_grp)
def do_stuff(grp, m_grp):
    g_dist = l_grp[m_grp == grp]

    for i in range(0,len(g_dist)):
        sys.stdout.write(str(g_dist[i]) + " ")
    print("")
    return g_dist
    
for grp in list(set(b_grp)):
    sys.stdout.write("bayes1 ")
    g_dist = do_stuff(grp, b_grp)
    

    sys.stdout.write("bayes2 ")
    global_dist = []
    for i in list(set(l_grp)):
        gd = float(sum(g_dist ==i))/ float(sum(l_grp == i))
        global_dist.append(gd)
        sys.stdout.write(str(gd) + " ")
    print("")

for grp in list(set(m_grp)):
    sys.stdout.write("mdl ")
    g_dist = do_stuff(grp, m_grp)
    
    sys.stdout.write("mdl2 ")
    global_dist = []
    for i in list(set(l_grp)):
        gd = sum(g_dist ==i)/ sum(l_grp == i)
        global_dist.append(gd)
        sys.stdout.write(str(gd) + " ")
    print("")

