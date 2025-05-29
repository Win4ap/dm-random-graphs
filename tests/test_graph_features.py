# test_graph_features.py
import networkx as nx
from graph_utils.graph_features import (
    min_degree,
    num_triangles,
    chromatic_number,
    clique_number,
    max_independent_set_size,
    domination_number,
    min_clique_cover_size,
)


def test_min_degree():
    G = nx.complete_graph(5)  # Все степени = 4
    assert min_degree(G) == 4

    G = nx.path_graph(3)  # Степени [1, 2, 1]
    assert min_degree(G) == 1


def test_num_triangles():
    G = nx.complete_graph(5)  # C(5,3) = 10 треугольников
    assert num_triangles(G) == 10

    G = nx.cycle_graph(4)  # 0 треугольников
    assert num_triangles(G) == 0


def test_chromatic_number():
    G = nx.complete_graph(3)  # Хроматическое число = 3
    assert chromatic_number(G) == 3

    G = nx.Graph()
    G.add_edges_from([(0, 2), (0, 3), (1, 2), (1, 3)])  # Двудольный, число = 2
    assert chromatic_number(G) == 2


def test_clique_number():
    G = nx.complete_graph(4)  # Клика размера 4
    assert clique_number(G) == 4

    G = nx.cycle_graph(5)  # Максимальная клика = 2 (рёбра)
    assert clique_number(G) == 2


def test_max_independent_set_size():
    G = nx.path_graph(3)  # Независимое множество {0, 2}
    assert max_independent_set_size(G) == 2


def test_domination_number():
    G = nx.star_graph(4)  # Центр доминирует всех
    assert domination_number(G) == 1


def test_min_clique_cover_size():
    G = nx.complete_graph(3)  # 1 клика
    assert min_clique_cover_size(G) == 1

    G = nx.path_graph(3)  # 2 клики (рёбра)
    assert min_clique_cover_size(G) == 2
