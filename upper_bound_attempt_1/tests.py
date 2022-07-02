import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
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
graph = nx.Graph()
edges = [(0, 1), (0, 2), (1, 2)]
graph.add_edges_from(edges)
# visualize the graph
# nx.draw(graph, with_labels=True, node_color="#dae05a")
# plt.show()
matrix_0 = helpers.graph_to_matrix(graph, 3)
matrix_0_cliques = [[0, 1, 2]]

graph = nx.Graph()
edges = [(0, 2), (0, 3), (0, 4), (1, 4), (2, 3), (3, 4)]
graph.add_edges_from(edges)
# nx.draw(graph, with_labels=True, node_color="#dae05a")
# plt.show()
matrix_1 = helpers.graph_to_matrix(graph, 5)
matrix_1_cliques = [[0, 2, 3], [0, 3, 4]]

graph = nx.Graph()
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
graph.add_edges_from(edges)
# nx.draw(graph, with_labels=True, node_color="#dae05a")
# plt.show()
matrix_2 = helpers.graph_to_matrix(graph, 4)
matrix_2_cliques = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]

# testcase 0 for find_subgraphs
result = helpers.find_subgraphs(matrix_0, 3, 1)
assert len(result) == len(matrix_0_cliques)
for i in range(len(result)):
  assert result[i] == matrix_0_cliques[i]

# testcase 1 for find_subgraphs
result = helpers.find_subgraphs(matrix_1, 3, 1)
result.sort()
assert len(result) == len(matrix_1_cliques)
for i in range(len(result)):
  assert result[i] == matrix_1_cliques[i]

# testcase 2 for find_subgraphs
result = helpers.find_subgraphs(matrix_2, 3, 1)
result.sort()
assert len(result) == len(matrix_2_cliques)
for i in range(len(result)):
  assert result[i] == matrix_2_cliques[i]



# Test for check_clique
new_row_0_a = [1, 1, 0]
new_row_0_b = [1, 1, 1]
assert helpers.check_clique(matrix_0_cliques, new_row_0_a, 1) == False
assert helpers.check_clique(matrix_0_cliques, new_row_0_b, 1) == True
new_row_1_a = [0, 0, 0, 0, 0]
new_row_1_b = [1, 0, 0, 1, 1]
assert helpers.check_clique(matrix_1_cliques, new_row_1_a, 1) == False
assert helpers.check_clique(matrix_1_cliques, new_row_1_b, 1) == True
