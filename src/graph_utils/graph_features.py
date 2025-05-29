import numpy as np
import networkx as nx
from collections import Counter
from networkx.algorithms.approximation.dominating_set import min_weighted_dominating_set
from networkx.algorithms import maximal_independent_set
import math


def compute_stats(arr):
    """
    Функция для вычисления основных статистик
    """
    mean = np.mean(arr)
    var = np.var(arr, ddof=1)
    std = math.sqrt(var)
    se = std / math.sqrt(len(arr))
    return mean, var, std, se


def min_degree(G: nx.Graph) -> int:
    """
    Функция для минимальной степени вершины графа G
    """
    return min(deg for _, deg in G.degree())


def num_triangles(G: nx.Graph) -> int:
    """
    Функция для вычисления количества треугольников графа G
    """
    return sum(dict(nx.triangles(G)).values()) // 3


def chromatic_number(G: nx.Graph) -> int:
    """
    Функция для поиска хроматического числа графа G
    """
    coloring = nx.coloring.greedy_color(G, strategy="largest_first")
    return max(coloring.values(), default=-1) + 1


def clique_number(G: nx.Graph) -> int:
    """
    Функция для поиска кликового числа графа G
    """
    Gc = nx.complement(G)
    coloring = nx.coloring.greedy_color(Gc, strategy="largest_first")
    counts = Counter(coloring.values())
    return max(counts.values(), default=0)


def max_independent_set_size(G: nx.Graph) -> int:
    """
    Функция для поиска размера максимального
    независимого множества графа G
    """
    mis = maximal_independent_set(G)
    return len(mis)


def domination_number(G: nx.Graph) -> int:
    """
    Функция для поиска числа
    доминирования для графа G
    """
    D = min_weighted_dominating_set(G)
    return len(D)


def min_clique_cover_size(G: nx.Graph) -> int:
    """
    Функция для поиска размера максимального
    кликового покрытия графа G
    """
    Gc = nx.complement(G)
    coloring = nx.coloring.greedy_color(Gc, strategy="largest_first")
    return len(set(coloring.values()))
