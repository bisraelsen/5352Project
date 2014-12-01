#!/usr/bin/env python

from pylab import savefig
from vbmod import *

from graph_tool.all import *
import os

g1f = 'bowtie.xml.gz'
g2f = 'karate_club_edges.xml.gz'
g3f = 'RLT_c_4_g_30.xml.gz'
g4f = 'RLT_c_4_g_15.xml.gz'
g5f = 'RLT_c_40_g_3.xml.gz'
g6f = 'RLT_c_40_g_30.xml.gz'

gList = [g1f,g2f,g3f,g4f,g5f,g6f]

# g1 = load_graph(gList[2])
# g = collection.data["football"]

for (gName,g) in ([(x,load_graph(x)) for x in gList] + collection.data.items()):
    A = adjacency(g)
    # graph_draw(g)
    
    N=A.shape[0]        # number of nodes
    Kvec=range(1,40+1) # range of K values over which to search
    
    # hyperparameters for priors
    net0={}
    net0['ap0']=N*1.
    net0['bp0']=1.
    net0['am0']=1.
    net0['bm0']=N*1.
    
    # options
    opts={}
    opts['NUM_RESTARTS']=25
    
    # run vb
    (net,net_K)=learn_restart(A,Kvec,net0,opts)
    
    # display figures
    restart_figs(A,net,net_K)
    dirname = "Bayes/" + gName.strip(".xml.gz")
    try:
        print("mkdir " + dirname)
        os.mkdir(dirname)
    except Exception as e:
        print("Directory already exists")

    f = open( dirname + "/net.txt", "w")
    f.write("Net = " + str(net))
    f.close()

    savefig(dirname + "/figure.png");
