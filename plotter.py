#!/usr/bin/env python

from pylab import savefig
from vbmod import *
import pickle

from graph_tool.all import *
import os
import sys

print (sys.argv[1])
gName = sys.argv[1]

if gName in collection.data.keys():
    g = collection.data[gName]
else:
    g = load_graph(gName + ".xml.gz")

A = adjacency(g)
N=A.shape[0]        # number of nodes

dirname_b = "Bayes/" + gName.strip(".xml.gz")
dirname_m = "MDL/" + gName.strip(".xml.gz")

g = GraphView(g, vfilt=label_largest_component(GraphView(g, directed=False)))

k_b = int( open(dirname_b + "/net.txt.k").read() )
try:
    k_m = pickle.load( open(dirname_m + "/mat.p") ).get_shape()[0]

    state = BlockState( g, B=g.num_vertices(), deg_corr=True )

    state_b = multilevel_minimize(state, B=k_b);
    state_m = multilevel_minimize(state, B=k_m);

    pos = sfdp_layout( g )

    g.vp['bayes'] = state_b.get_blocks()
    g.vp['mdl'] = state_m.get_blocks()
    g.vp['pos'] = pos

    g.gp['k_b'] = g.new_graph_property('int', k_b)
    g.gp['k_m'] = g.new_graph_property('int', k_m)

    graph_draw(g,pos=pos,vertex_fill_color=state_b.get_blocks(), output=dirname_b+ "/" + gName.strip(".xml.gz") + ".pdf")
    graph_draw(g,pos=pos,vertex_fill_color=state_b.get_blocks(), output=dirname_b+ "/" + gName.strip(".xml.gz") + ".png")

    graph_draw(g,pos=pos,vertex_fill_color=state_m.get_blocks(), output=dirname_m+ "/" + gName.strip(".xml.gz") + ".pdf")
    graph_draw(g,pos=pos,vertex_fill_color=state_m.get_blocks(), output=dirname_m+ "/" + gName.strip(".xml.gz") + ".png")

    g.save(gName.strip(".xml.gz") + ".g.xml.gz")

except IOError as e:
    print (e)

