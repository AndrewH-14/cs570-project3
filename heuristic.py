"""
Program that will solve the graph coloring problem using the provided graph as
input.

Written by: Andrew Hankins

Running the program:
python3 heuristic.py <graph file> <y/n diagram>
"""
import sys
import networkx as nx
import matplotlib.pyplot as plt

def init_coloring(vertices):
    """
    Function that will initialize a coloring array to all zeros.
    Parameters:
    -----------
        num_vertices: int
            The number of vertices in the graph which will be used to size the array.
    Returns:
    --------
        array: The initialized coloring array.
    """
    coloring = {}
    for vertex in vertices:
        coloring[vertex] = 0
    return coloring

def color_vertex(vertex, max_colors, coloring, graph):
    """
    Will attempt to color the provided vertex given the maximum number of
    colors allowed.
    Parameters:
    -----------
        vertex: int
            The key of the vertex we are attempting to color.
        max_colors: int
            The maximum number of colors that can be used.
        coloring: arr
            The current coloring of the graph. 0 represents an uncolored vertex.
        graph: dict
            The graph we are attempting to color.
    Returns:
    --------
        bool: Whether or not the vertex was able to be colored.
    """
    # Get a list of the possible colors
    remaining_colors = []
    for color in range(1, max_colors+1):
        remaining_colors.append(color)
    # Loop through each neighbor to get a list of remaining colors
    for neighbor in graph[vertex]:
        if coloring[neighbor] in remaining_colors:
            remaining_colors.remove(coloring[neighbor])
    # If any coloring remain color using the lowest number
    if len(remaining_colors) > 0:
        coloring[vertex] = remaining_colors[0]
        return True
    else:
        return False

def heuristic_search(graph):
    """
    Function that will use a heuristic to search for a solution to the graph
    coloring problem.
    Parameters:
    -----------
        Graph: dictionary
            The graph to find a solution for.
    Returns:
    --------
        int: The number of colors used in the solution.
        arr: The coloring of the graph in array form.
    """
    # Sorted vertices by their number of neighbors
    vertices_neighbors = {}
    for vertex in graph:
        vertices_neighbors[vertex] = len(graph[vertex])
    sorted_list = sorted(vertices_neighbors.items(), key = lambda kv: kv[1], reverse=True)
    # Determine the number of colors to start with
    max_colors = 1
    # Loop until a solution is found
    solution_found = False
    while not solution_found:
        # Initialize coloring to blank values (0)
        coloring = init_coloring(graph.keys())
        # Attempt to color the sorted list
        for vertex in sorted_list:
            if not color_vertex(vertex[0], max_colors, coloring, graph):
                solution_found = False
                max_colors += 1
                break
            solution_found = True

    return max_colors, coloring

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

def main():
    """
    The main function for the program.
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

    k, coloring = heuristic_search(graph)
    print(f"Chromatic number: {k}")
    print(f"Coloring: {coloring}")

    # Provide a diagram of the graph if requested
    if sys.argv[2] == 'y':
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

if __name__ == "__main__":
    main()
