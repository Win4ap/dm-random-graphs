import numpy as np
from sklearn.neighbors import NearestNeighbors
import networkx as nx


def build_knn_graph(k, vertices):
    v = np.asarray(vertices, dtype=float).reshape(-1, 1)
    n = v.shape[0]

    nbrs = NearestNeighbors(n_neighbors=k + 1).fit(v)
    distances, indices = nbrs.kneighbors(v)

    G = nx.Graph()
    G.add_nodes_from(range(n))

    for i in range(n):
        for j in indices[i][1:]:
            G.add_edge(i, j)

    return G


def build_distance_graph(d, vertices):
    v = np.asarray(vertices)
    n = v.size

    G = nx.Graph()
    G.add_nodes_from(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if abs(v[i] - v[j]) <= d:
                G.add_edge(i, j)

    return G
