#!/usr/bin/env python

import graphviz
#import networkx as nx
#import matplotlib.pyplot as plt
import csv

FILENAME="test/list2.csv"
OUTNAME="test/graphviz_out.png"

def read_edges(filename):
    edges = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            edges.append(row)
    return edges


#def add_edges(graph, edge_list):
#    for e in edge_list:
#        print(node)
#        graph.add_edge(e)
#    return graph
#
#
#def print_plot(graph):
#    nx.draw(graph, with_labels=True)
#    plt.savefig(OUTNAME)


if __name__ == "__main__":
    g = graphviz.Digraph("G", comment="Test", format="png")
    edges = read_edges(FILENAME)
    for edge in edges:
        g.edge(edge[0], edge[1])

    g.render(directory="test").replace("\\", "/")

    #G = nx.Graph()
    #G.add_edges_from(edges)
    #print_plot(G)



