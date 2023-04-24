import networkx as nx
import matplotlib.pyplot as plt

def create_graph(graph, coloring):
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
