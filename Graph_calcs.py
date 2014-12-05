#!/usr/bin/env python

from vbmod import *
import matplotlib.pyplot as plt
from graph_tool.all import *
import numpy as np
import sys
import scipy

graph_loc = sys.argv[1]
#graph_loc = "/home/brett/brett.israelsen@gmail.com/Education/Graduate/Fall 2014/CS5352/Project/saved_graphs/karate.g.xml.gz"
g = load_graph(graph_loc)
N = g.num_vertices()

b_grp = g.vp['bayes'].a
m_grp = g.vp['mdl'].a

def diffEdgeType(g,str_v_prop,grp_src):
    isDifferent = g.new_edge_property('bool')
    
    for e in g.edges():
        if g.vp[str_v_prop].a[e.source()] == grp_src or g.vp[str_v_prop].a[e.target()] == grp_src:
            if not g.vp[str_v_prop].a[e.source()] == g.vp[str_v_prop].a[e.target()]:
                isDifferent[e] = True
            else:
                isDifferent[e] = False
        else:
            isDifferent[e] = False
            
    return isDifferent
            
def do_stuff(grp, m_grp,strProp):
    nvN = sum(m_grp == grp)/float(N)
    sys.stdout.write(str(nvN) + " ")
    
    g2 = GraphView(g, vfilt=lambda e: m_grp[e] == grp)
    avg = vertex_average(g2, 'total')
    sys.stdout.write(str(avg[0]) + " ")
    sys.stdout.write(str(avg[1]) + " ")
    
    ed = g2.num_edges() / scipy.misc.comb(g2.num_vertices(), 2)
    sys.stdout.write(str(ed))

    E = g2.num_edges()
    g3 = GraphView(g,efilt = diffEdgeType(g, strProp,grp))
    E_dens = float(E)/float(g3.num_edges())
    sys.stdout.write(str(E_dens))
    print("")

for grp in list(set(b_grp)):
    sys.stdout.write("bayes ")
    do_stuff(grp, b_grp,'bayes')


for grp in list(set(m_grp)):
    sys.stdout.write("mdl ")
    do_stuff(grp, m_grp,'mdl')
