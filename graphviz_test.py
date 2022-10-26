#!/usr/bin/env python

import graphviz
import csv

FILENAME="generators/list2.csv"
OUTNAME="out/graphviz_out.png"

def read_edges(filename):
    edges = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            edges.append(row)
    return edges


if __name__ == "__main__":
    g = graphviz.Digraph("G", comment="Test", format="png")
    edges = read_edges(FILENAME)
    for edge in edges:
        g.edge(edge[0], edge[1])

    g.render(directory="out")

