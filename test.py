#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plt
import csv

FILENAME="list.csv"

def read_edges(filename):
    edges = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            t = tuple(e for e in row)
            edges.append(t)
    return edges


def add_edges(graph, edge_list):
    for e in edge_list:
        print(node)
        graph.add_edge(e)
    return graph


def print_plot(graph):
    nx.draw(graph, with_labels=True)
    plt.savefig("out.png")


if __name__ == "__main__":
    G = nx.Graph()
    edges = read_edges(FILENAME)
    G.add_edges_from(edges)
    print_plot(G)

