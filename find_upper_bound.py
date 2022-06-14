import networkx as nx
import numpy as np
import math
import helpers

# searching for additional with maximum degree s.t.
# it doesn't create clique of size n
# value is the the color of edge
def search_all(matrix, n, value):
  small_cliques = helpers.find_subgraphs(matrix, n-1, 1)
  upper_bound = 0
  results = []
  for i in range(1, 2**35):
    bin_str = "{0:b}".format(i)
    bin_str = bin_str[::-1]
    new_row = np.zeros(len(matrix))
    for j in range(len(bin_str)):
      if (bin_str[j] == '1'):
        new_row[j] = 1
    new_size = 0
    for j in range(len(new_row)):
      if (new_row[j] == value): new_size += 1 
    if (new_size < upper_bound): continue
    if not helpers.check_clique(small_cliques, new_row, 1):
      if (new_size > upper_bound):
        upper_bound = new_size
        results = [new_row]
      elif (new_size == upper_bound):
        results.append(new_row)
  return results
  



matrices = helpers.read_graph_to_matrix("r46_35some.g6", 35)

result = search_all(matrices[0], 4, 1)