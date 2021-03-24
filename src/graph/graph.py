import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.drawing.nx_agraph import write_dot
from networkx.drawing.nx_agraph import read_dot
import string
import random

ALPHABET_SIZE=4

def add_random_data(graph):
    for node in graph.nodes:
        # seq = range(1,4)
        len_seq = 4
        graph.nodes[node]["len"] = len_seq
        graph.nodes[node]["seq"] = float("".join([str(x) for x in random.choices(range(ALPHABET_SIZE), k=len_seq)]))

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
    # graph.nodes[0]["test"] = "test2"


def generate_graph(values, graph_name):
    try:
        values = [int(x) for x in values]
    except ValueError as e:
        raise
    G = nx.DiGraph()
    G.add_nodes_from(range(values[0]))
    add_random_edges(G, values[1])
    add_random_data(G)
    add_color(G)
    write_dot(G, graph_name)
    

def insert_edge(name, from_edge, to_edge):
    name_trimmed = name[1:] # We ignore the leading slash
    G = nx.DiGraph(read_dot(name_trimmed))
    G.add_edge(int(from_edge), int(to_edge))
    add_color(G)
    write_dot(G, name_trimmed)

def delete_edge(name, from_edge, to_edge):
    name_trimmed = name[1:] # We ignore the leading slash
    G = nx.DiGraph(read_dot(name_trimmed))
    print(G.edges)
    G.remove_edge(from_edge, to_edge)
    add_color(G)
    write_dot(G, name_trimmed)

def add_color(graph):
    for node in graph.nodes:
        if len(graph.in_edges(node)) + len(graph.out_edges(node)) <= 1 :
            graph.nodes[node]["color"] = "red"
        else:
            graph.nodes[node]["color"] = "#ADD8E6"

def refresh_colors(name):
    name_trimmed = name[1:]
    G = nx.DiGraph(read_dot(name_trimmed))
    add_color(G)
    write_dot(G, name_trimmed)
    