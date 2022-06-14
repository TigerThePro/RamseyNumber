import networkx as nx
import numpy as np
import math
import helpers

# searching for additional node with maximum degree s.t.
# it doesn't create clique of size n
# value is the the color of edge
# write to result/[address].txt
def search(matrix, n, value, address):
  small_cliques = helpers.find_subgraphs(matrix, n-1, 1)
  bound = [0]
  row = np.zeros(len(matrix))
  row[0] = value
  search_helper(small_cliques, row, value, bound, address)
  return


def search_helper(small_cliques, row, value, bound, address):
  if (row[-1] == value): 
    return
  rightmost = 0
  for i in range(len(row)):
    if (row[i] == value):
      rightmost = i
  for i in range(rightmost+1, len(row)):
    row_copy = row.copy()
    row_copy[i] = value
    occ = 0
    for i in range(len(row)):
      if (row_copy[i] == value): occ += 1

    # # if it's impossible to exceed bound, 
    # # even with all remaining elemnts == value
    # # then return
    # if (occ + (len(row) - i - 1) <= bound[0]): 
    #   print(str((occ + (len(row) - i - 1))))
    #   print(str(i))
    #   return

    # check if row is working
    if helpers.check_clique(small_cliques, row_copy, value):
      return
    
    # check if it's a new bound
    if (occ > bound[0]):
      bound[0] = occ
      f = open("result/" + address, 'w')
      f.write("Bound = " + str(bound[0]))
      f.write("\n")
      f.write(str(row_copy))
      f.close()

    search_helper(small_cliques, row_copy, value, bound, address)



matrices = helpers.read_graph_to_matrix("r46_35some.g6", 35)

result = search(matrices[0], 4, 1, "upperbound_color1")