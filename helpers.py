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


# TODO
# change to parameter to what you think is needed
# you can use this as a dummy function for the search
def search():
  return



