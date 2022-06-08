import networkx as nx
import numpy as np
import os

# input address to .g6 k_n file
# output a list of adjcency matrices (numpy matrices)
# input an absolute path to ensure working
def graph_to_matrix(address, n):
  graphs = nx.read_graph6(address)
  matrices = []
  for graph in graphs:
    matrix = np.zeros(shape=(n,n))
    for i in range(len(graph.nodes)):
      nbrs = list(graph.neighbors(i))
      for nbr in nbrs:
        matrix[nbr][i] = 1
        matrix[i][nbr] = 1
    for i in range(n):
      for j in range(n):
        if (i != j and matrix[i][j] != 1):
          matrix[i][j] = -1
    matrices.append(matrix)
  return matrices


# test for graph to mateix
produced = graph_to_matrix("r46_35some.g6", 35)
graphs = nx.read_graph6("r46_35some.g6")
assert len(produced) == len(graphs)
for i in range(len(produced)):
  for j in range(35):
    for k in range(35):
      if j == k:
        assert produced[i][j][k] == 0
      elif produced[i][j][k] == 1:
        assert graphs[i].has_edge(j, k)



