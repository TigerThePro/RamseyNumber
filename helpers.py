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


# take in adj matrix, int n, value
# return a list, where each element is a n tuple
# each element is a size n clique found in the adj matrix
# will use this as preprocessing in search to reduce 
# time spent on checking cliques
# two nodes i,j are adjacent if matrix[i][j] == value
def find_subgraphs(matrix, n, value):
  acc = [[]]
  result = []
  if (n == 0): return result
  for i in  range(len(matrix)):
    size = len(acc)
    if size == 0:
      acc.append([i])
      continue
    for j in range(size):
      sub_size = len(acc[j])
      good = True
      for k in range(sub_size):
        if matrix[i][acc[j][k]] != value:
          good = False
          break
      if good:
        new_list = acc[j].copy()
        new_list.append(i)
        if (len(new_list) == n):
          result.append(new_list)
        else:
          acc.append(new_list)
  return result


# input small_cliques (output of find_subgraphs), row, value
# make sure the new node (the row) does not form a clique
# with any of the previous clique
# if row[i] == value, then new node is adjacent with node i
# if clique formed return true
# else return false
def check_clique(small_cliques, row, value):
  for clique in small_cliques:
    no_clique = False
    for i in range(len(clique)):
      if row[clique[i]] != value:
        no_clique = True
    if not no_clique:
      return True
  return False

  



