#!/usr/bin/env python

from vbmod import *
import matplotlib.pyplot as plt
from graph_tool.all import *
import sys
import scipy


graph_loc = sys.argv[1]

g = load_graph(graph_loc)
N = g.num_vertices()

b_grp = g.vp['bayes'].a
m_grp = g.vp['mdl'].a


def do_stuff(grp, m_grp):
    nvN = sum(m_grp == grp)/float(N)
    sys.stdout.write(str(nvN) + " ")
    g2 = GraphView(g, vfilt=lambda e: m_grp[e] == grp)
    avg = vertex_average(g2, 'total')
    sys.stdout.write(str(avg[0]) + " ")
    sys.stdout.write(str(avg[1]) + " ")
    
    ed = g2.num_edges() / scipy.misc.comb(g2.num_vertices(), 2)
    sys.stdout.write(str(ed))
    print("")


for grp in list(set(b_grp)):
    sys.stdout.write("bayes ")
    do_stuff(grp, b_grp)


for grp in list(set(m_grp)):
    sys.stdout.write("mdl ")
    do_stuff(grp, m_grp)
