import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def add_random_edges(graph, n):
    edges = []

    for i in range(n):
        new_edge = (np.random.randint(0, graph.number_of_nodes() + 1),
                    np.random.randint(0, graph.number_of_nodes() + 1))
        while new_edge in graph.edges:
            new_edge = (np.random.randint(0, graph.number_of_nodes() + 1),
                        np.random.randint(0, graph.number_of_nodes() + 1))
        edges.append(new_edge)
    graph.add_edges_from(edges)


def generate_button(values):
    try:
        values = [int(values[x]) for x in values]
    except ValueError:
        print("Please enter a valid number in the input boxes")
    G = nx.DiGraph()
    G.add_nodes_from(range(values[0]))
    G.add_edge(0, 1)
    add_random_edges(G, values[1])
    nx.draw(G, with_labels=True)
    plt.show()
