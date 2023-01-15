import numpy as np
import math
import networkx as nx


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
    T = transition_matrix(g1)
    V = page_rank(T)
    print("Final Rank:\n", V)


if __name__ == "__main__":
    main()
