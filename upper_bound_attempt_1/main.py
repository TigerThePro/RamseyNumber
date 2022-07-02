from multiprocessing.spawn import prepare
from operator import truediv
import networkx as nx
import numpy as np
import helpers
import random
import math
import copy

# you can write your program here
def find_maximal_good_vector(matrix, size, initial, best):
    # DFS, keeps track of best (most coloured) entries (or a list of them)
    return best

# takes matrix and checks all submatrices of size. Returns true if no complete submatrices of one colour, else false
def is_good_colouring_single(matrix, size):
    n = matrix.shape[0]
    vertices = []
    for i in range(n - 1):
        vertices.append(i)
    count = max(math.comb(n - 1, size - 1), 0)
    selected_list = []
    clique = complete_clique(size, 1)

    if size > n:
        return True

    if size == n:
        for j in range(n):
            for k in range(n):
                if clique[j][k] != matrix.item(j, k):
                    return False
        return True
    
    while len(selected_list) < count:
        selected = copy.deepcopy(vertices)
        random.shuffle(selected)
        selected = selected[0:n - size]
        if new_includes(selected_list, selected):
            continue
        else:
            selected_list.append(selected)
        matrix_copy = copy.deepcopy(matrix)
        submatrix = submatrix_builder(matrix_copy, selected)
        match = True
        for j in range(submatrix.shape[0]):
            for k in range(submatrix.shape[0]):
                if clique[j][k] != submatrix.item(j, k):
                    match = False
                    break
            if not match:
                break
        if match:
            return False
    return True

# returns a adjacency matrix of size all one colour
def complete_clique(size, colour):
    matrix = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if i < j:
                matrix[i, j] = colour
    return matrix

# Checks if sub_list is an element of main_list
def new_includes(main_list, sub_list):
    for i in range(len(main_list)):
        if len(main_list[i]) != len(sub_list):
            continue
        else:
            for j in range(len(sub_list)):
                if main_list[i][j] == sub_list[j]:
                    if j == len(sub_list) - 1:
                        return True
                else:
                    break
    return False

# returns a submatrix with the indexed columns removed from the original matrix
def submatrix_builder(matrix, columns):
    columns.sort()
    for column in columns[::-1]:
        matrix = remove_column(matrix, column)
        matrix = np.delete(matrix, column, 0)
    return matrix

def remove_column(matrix, index):
    return np.delete(matrix, index, 1)

def summation(a, b):
    return a + b

# Takes binary array and shifts leading 1 over to next open spot
def step_digit(previous):
    count = 0
    sum = reduce(previous, summation)
    add = False
    for i in range(len(previous)):
        if add and previous[i] == 0:
            previous[i] = 1
            break
        if previous[i] == 1 and not add:
            count += 1
            if count == sum:
                if i == len(previous) - 1:
                    return False
                add = True
                previous[i] = 0
    return previous

# Takes binary array and add 1 over to next open spot after leading 1
def add_digit(previous):
    count = 0
    sum = reduce(previous, summation)
    add = False
    for i in len(previous):
        if add:
            previous[i] = 1
            break
        if previous[i] == 1:
            count += 1
            if count == sum:
                if i == len(previous) - 1:
                    return False
                add = True
    return previous