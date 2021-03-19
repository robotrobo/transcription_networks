import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.drawing.nx_agraph import write_dot
from networkx.drawing.nx_agraph import read_dot


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
    

def insert_edge(name, from_edge, to_edge):
    name_trimmed = name[1:] # We ignore the leading slash
    G = nx.DiGraph(read_dot(name_trimmed))
    G.add_edge(int(from_edge), int(to_edge))
    write_dot(G, name_trimmed)