# test_graph_generation.py
from graph_utils.graph_generation import build_knn_graph, build_distance_graph


def test_build_knn_graph():
    vertices = [1, 2, 3, 10, 20, 30]
    G = build_knn_graph(k=2, vertices=vertices)
    assert G.number_of_nodes() == 6
    assert G.number_of_edges() >= 6  # Каждая вершина имеет 2 соседа


def test_build_distance_graph():
    vertices = [1, 2, 3, 10, 20, 30]
    G = build_distance_graph(d=5.0, vertices=vertices)
    assert G.number_of_nodes() == 6
    assert G.has_edge(0, 1)  # |1-2| <= 5
    assert not G.has_edge(0, 3)  # |1-10| > 5
