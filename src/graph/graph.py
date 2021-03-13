import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.drawing.nx_agraph import write_dot


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
    graph.nodes[0]["test"] = "test2"


def generate_graph(values, graph_name):
    try:
        values = [int(x) for x in values]
    except ValueError as e:
        raise
    G = nx.DiGraph()
    G.add_nodes_from(range(values[0]))
    add_random_edges(G, values[1])
    write_dot(G, graph_name)