"""
Module that defines utility functions in regards to graphs.

Written by: Andrew Hankins
"""
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(graph, coloring):
    """
    Function that will create a visualization of a graph using the networkx
    module.
    Parameters:
    -----------
        graph : dictionary
            The graph that will be visualized.
        coloring : dictionary
            The coloring of the provided graph.
    Returns:
    --------
        None
    """
    # Create a NetworkX graph object
    G = nx.Graph()
    # Add vertices and edges to the graph
    for vertex, neighbors in graph.items():
        G.add_node(vertex)
        for neighbor in neighbors:
            G.add_edge(vertex, neighbor)
    # Set the color for each vertex based on the coloring
    color_map = [coloring[node] for node in G.nodes]
    # Draw the graph
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, node_color=color_map, with_labels=True, cmap=plt.cm.jet)
    plt.show()
    return

def print_graph(graph):
    """
    Prints off the graph.
    Parameters:
    -----------
        graph
    Returns:
    --------
        None
    """
    for vertex in graph:
        print(f"{vertex}: {graph[vertex]}")
    return

def read_graph_from_file(file_name):
    """
    Function that will read a graph input file and store it in a dictionary.

    Note: For more info about the input file format look at the README.md

    Parameters:
    -----------
        file_name : str
            The name of the input file that contains the graph.
    Returns:
    --------
        dictionary : A representation of the graph, where each key represents a vertex
                     and each item is a list of the vertex's neigbors.
    """
    graph = {}
    # Open the specifed file in order to read its data
    with open(file_name, 'r') as file:
        # Number of vertices should be the first line in the file
        file.readline()
        num_vertices = int(file.readline())
        # Read each line in one by one and add each node to the list of neigbors
        # as necessary
        for line in file:
            if line[0] == '$':
                # Break condtion encountered, no more data remains
                break
            else:
                data = line.split(" ")
                node1 = int(data[0])
                node2 = int(data[1])
                if node1 in graph:
                    if node2 not in graph[node1]:
                        graph[node1].append(node2)
                else:
                    graph[node1] = [node2]
                if node2 in graph:
                    if node1 not in graph[node2]:
                        graph[node2].append(node1)
                else:
                    graph[node2] = [node1]
    return graph
