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

    print(T)


def main():
    g1 = np.array([[0, 1, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [1, 0, 0, 0]])
    transition_matrix(g1)


if __name__ == "__main__":
    main()
