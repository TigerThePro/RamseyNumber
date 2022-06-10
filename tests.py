import networkx as nx
import numpy as np
import math
import time

import helpers
import main


graphs = nx.read_graph6("r46_35some.g6")

# test for graph to mateix
produced = helpers.read_graph_to_matrix("r46_35some.g6", 35)
assert len(produced) == len(graphs)
for i in range(len(produced)):
  for j in range(35):
    for k in range(35):
      if j == k:
        assert produced[i][j][k] == 0
      elif produced[i][j][k] == 1:
        assert graphs[i].has_edge(j, k)




# test for find_subgraphs