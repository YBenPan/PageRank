import numpy as np
import math
import networkx as nx
from tabulate import tabulate


def user_input():
    n = int(input("Enter the number of vertices: "))
    g = []
    for i in range(n):
        str = input(f"Row {i + 1}: ")
        arr = [int(s) for s in str.split(' ')]
        if len(arr) != n:
            raise ValueError("Input row size does not match matrix dimension. Exiting...")
        g.append(arr)
    M = np.array(g)
    return M


def transition_matrix(adj_matrix):
    """Create transition matrix from adjacency matrix"""
    # TODO: Check for strongly connectedness
    
    T = adj_matrix.copy()
    T = T.astype(float)
    nrows, ncols = T.shape
    assert nrows == ncols  # Check if adj_matrix is a square matrix
    n = nrows

    for i in range(n):
        T[i, :] /= np.sum(T[i])

    return T


def page_rank(transition_matrix, num_it=1000):
    T = transition_matrix.copy().T # Need to explain why transpose
    n = T.shape[0]
    print("Transition Matrix:\n", T)

    V = np.array([1 / n] * n)
    print("Rank vector:\n", V)

    for i in range(num_it):
        V = np.matmul(T, V)

    return V


def main():
    g1 = np.array([[0, 1, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [1, 0, 0, 0]])
    G = user_input()
    print("Adjacency Matrix:\n", G)
    T = transition_matrix(G)
    V = page_rank(T)
    print("Final Rank:\n", V)


if __name__ == "__main__":
    main()
