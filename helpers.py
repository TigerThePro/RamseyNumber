import networkx as nx
import numpy as np
import os

# input address to .g6 k_n file
# output a list of adjcency matrices (numpy matrices)
# input an absolute path to ensure working
def read_graph_to_matrix(address, n):
  graphs = nx.read_graph6(address)
  matrices = []
  for graph in graphs:
    matrices.append(graph_to_matrix(graph, n))
  return matrices


# take networkx graph, and return adj matrix
# 1 for adj with first color, -1 for second color
def graph_to_matrix(graph, n):
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
  return matrix


# TODO
# take in adj matrix, int n
# return a list, where each element is a n tuple
# each element is a size n clique found in the adj matrix
# will use this as preprocessing in search to reduce 
# time spent on checking cliques
def find_subgraphs(matrix, n):
  return []



