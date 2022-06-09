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
    vertices = []
    for i in range(len(matrix) - 1):
        vertices.append(i)
    count = max(math.comb(len(matrix) - 1, size - 1), 0)
    selected_list = []
    clique = complete_clique(size, 1)

    if size > len(matrix):
        return True

    if size == len(matrix):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if clique[j][k] != matrix[i][j]:
                    return False
        return True
    
    while len(selected_list) < count:
        selected = copy.deepcopy(vertices)
        random.shuffle(selected)
        selected = selected[0:len(matrix) - size]
        if new_includes(selected_list, selected):
            continue
        else:
            selected_list.append(selected)
        matrix_copy = copy.deepcopy(matrix)
        submatrix = submatrix_builder(matrix_copy, selected)
        match = True
        for j in range(len(submatrix)):
            for k in range(len(submatrix)):
                if clique[j][k] != submatrix[j][k]:
                    match = False
                    break
            if not match:
                break
        if match:
            return False
    return True

# returns a adjacency matrix of size all one colour
def complete_clique(size, colour):
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            if i >= j:
                matrix[i].append(0)
            else:
                matrix[i].append(colour)
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
    for column in reversed(columns):
        remove_column(matrix, column)
        del matrix[column]
    return matrix

def remove_column(matrix, index):
    for i in range(len(matrix)):
        row = matrix[i]
        del row[index]

def summation(a, b):
    return a + b

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


print(is_good_colouring_single(    [[0,-1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1],
    [0,0,-1,1,1,1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,1,-1,-1,1,1,1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1],
    [0,0,0,-1,1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1],
    [0,0,0,0,-1,-1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1],
    [0,0,0,0,0,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1],
    [0,0,0,0,0,0,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1],
    [0,0,0,0,0,0,0,-1,-1,1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1],
    [0,0,0,0,0,0,0,0,1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,1],
    [0,0,0,0,0,0,0,0,0,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,1,-1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,-1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,1,1,-1,1,1,-1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,1,-1,-1,-1,-1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,-1,-1,-1,-1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,1,-1,-1,-1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,-1,-1,-1,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,1,-1,-1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,-1,-1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], 6))