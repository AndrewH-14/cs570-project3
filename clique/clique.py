"""
"""
import sys
import networkx as nx
import matplotlib.pyplot as plt

def graph_coloring_to_clique(G, k):
    """
    """
    # Initialize the new graph that is going to be created
    H = {}
    # Add all the nodes that will be in the new graph
    for vertex in G:
        for i in range(k):
            H[str(vertex) + "-" + str(i + 1)] = []
    # Add all of the edges in the new graph
    for vertex in H:
        # Get a list of all the original vertices
        vertices = G.keys()
        # Get the original vertex
        vertex_in_G = int(str(vertex).split("-")[0])
        # Get the edges that the vertex is a neighbor with
        neighbors_in_G = G[vertex_in_G]
        # Update the list of vertices to only include non neighbors
        non_neighbors_in_G = {value for value in vertices if ((value not in neighbors_in_G) and (vertex_in_G != value))}
        # If {v1, v2} is not an edge in the G, make it an edge in H
        for vertex2 in H:
            vertex2_in_G = int(str(vertex2).split("-")[0])
            if vertex2_in_G in non_neighbors_in_G:
                H[vertex].append(vertex2)
            else:
                color1 = int(str(vertex).split("-")[1])
                color2 = int(str(vertex2).split("-")[1])
                if (vertex_in_G != vertex2_in_G) and (color1 != color2):
                    H[vertex].append(vertex2)
    return H

def print_graph(graph):
    """
    Prints of the graph.
    Parameters:
    -----------
        Graph: dictionary
            The graph to find a solution for.
    """
    for vertex in graph:
        print(f"{vertex}: {graph[vertex]}")
    return

def read_graph(file):
    """
    """
    graph = {}
    file_name  = sys.argv[1]
    with open(file_name, 'r') as file:
        num_vertices = int(file.readline())
        for line in file:
            if line[0] == '$':
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

def write_to_file(graph, k):
    """
    """
    # Convert graph to form that can be stored in a data file
    output_lines = [f"{len(graph)}\n"]
    for node, neighbors in graph.items():
        file_node = (int(str(node).split("-")[0]) * k) - (k - (int(str(node).split("-")[1])))
        for neighbor in neighbors:
            file_neighbor = (int(str(neighbor).split("-")[0]) * k) - (k - (int(str(neighbor).split("-")[1])))
            if file_node < file_neighbor:
                output_lines.append(f"{file_node} {file_neighbor} 0\n")
    output_lines.append("$\n")
    with open("intermediate.txt", "w") as f:
        f.writelines(output_lines)

def main():
    """
    """
    file_name  = sys.argv[1]
    visual = sys.argv[2]
    k = int(sys.argv[3])
    G = read_graph(file_name)
    H = graph_coloring_to_clique(G, k)
    write_to_file(H, k)
    return

if __name__ == "__main__":
    main()
