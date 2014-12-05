from graph_tool.all import *
import sys

g = load_graph(sys.argv[1])    
#print("N = " + str(g.num_vertices()) + "E = " + str(g.num_edges()))
maxB = get_max_B(N=g.num_vertices(),E=g.num_edges())
print(maxB)

