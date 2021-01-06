import numpy as np
import glob
import matplotlib.pyplot as plt
import networkx as nx
import argparse
import os
from networkx.drawing.nx_pydot import write_dot, pydot_layout

def plot_flux_network(fluxmat,fraction=0.9603,direction=True):

    if direction:
        flux = nx.DiGraph()
    else:
        flux = nx.Graph()
    flux.graph["graph"] = {"rankdir": "LR"}

    ## Using the fraction to cut off the small flux
    if fraction != 1.0:
        fratot = np.sum(fluxmat)*fraction
        index = np.searchsorted(np.add.accumulate(np.sort(fluxmat.flatten())[::-1]), fratot)
        cutoff = np.sort(fluxmat.flatten())[::-1][index]
        fluxmat[np.where(fluxmat < cutoff)] = 0.0

    flux = network_add_node(flux)
    flux = network_add_edge(flux, fluxmat)
    write_dot(flux, "file.dot")

def network_add_node(flux):
    nodelist = []
    paramdict = {}
    for i in range(nstate):
        paramdict = {
        'image':pngfile[i],
        "label": "",
        'shape': "none"
        }
        nodelist.append((i, paramdict))
    flux.add_nodes_from(nodelist)
    return flux

def network_add_edge(flux, fluxmat):
    fluxmatwidth = fluxmat/np.sum(fluxmat)*5
    edge = [(i, j, {
        'penwidth': max(fluxmatwidth[i, j],0.05)*50,
        'label':"{:.2e}".format(fluxmat[i, j]),
        "color":"red", 
        'fontsize':"100", 
        "style":"bold",
         "arrowsize": 2
        })
        for i in range(nstate) for j in range(nstate) if fluxmat[i, j] > 0]
    flux.add_edges_from(edge)
    return flux
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw the transition pathway.')
    parser.add_argument('-i',"--input", type=str,
                        help='net flux input file')
    parser.add_argument('-d', "--directory", type=str, default="./",
                        help='The directory where the images has been putted, default is the current directory')
    args = parser.parse_args()
    inputfile = args.input
    directory = args.directory


    data = np.loadtxt(inputfile)
    nstate = data.shape[0]
    pngfile = sorted(glob.glob(os.path.join(directory,"state*.png")))
    plot_flux_network(data)
