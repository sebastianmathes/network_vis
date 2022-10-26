#!/usr/bin/env python3

import random

NODES=[
    "Node_A",
    "Node_B",
    "Node_C",
    "Node_D",
    "Node_E",
    "Node_F",
    "Node_G",
    "Node_H",
    "Node_I",
    "Node_J",
    "Node_K",
    "Node_L",
    "Node_M",
    "Node_N",
    "Node_O",
    "Node_P",
    "Node_Q",
    "Node_R",
    "Node_S",
    "Node_T",
    "Node_U",
    "Node_V",
    "Node_W",
    "Node_X",
    "Node_Y",
    "Node_Z",
]

edges = []
for i in range(0,40):
    e = random.sample(NODES, k=2)
    if e not in edges:
        edges.append(e)

with open ("test/list2.csv", "w") as outfile:
    for edge in edges:
        outfile.write(";".join(edge) + "\n")

