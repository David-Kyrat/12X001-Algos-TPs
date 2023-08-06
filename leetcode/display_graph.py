from typing import List, Tuple

import matplotlib.pyplot as plt
import networkx as nx


def display_graph(edges: List[Tuple[int, int]]):
    """Plots graph defined by given `edges` (with matplotlib)"""
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw_networkx(G)
    plt.show()


if __name__ == "__main__":
    graph = [(0, 2), (1, 2), (1, 3), (5, 3), (3, 4), (1, 0)]
    display_graph(graph)
