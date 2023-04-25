"""
Program that will map a graph coloring problem to the clique problem.

Written by: Andrew Hankins

Running the program:
python3 heuristic.py <data file> <y/n diagram> <num colors>
"""
import sys
sys.path.append('../')
import graph_util

def graph_coloring_to_clique(G, k):
    """
    Function that will map a graph coloring problem to the clique problem.
    Parameters:
    -----------
        G : dictionary
            The original graph that we are attempting to find the chromatic
            number for.
        k : int
            The number of colors that we would like to check.
    Returns:
    --------
        dictionary : The new graph that solving the clique problem for will
                     determine if it can be colored in k colors.
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

def write_to_file(graph, k):
    """
    Function that will write the new graph to an intermediate data file.
    Parameters:
    -----------
        graph : dictionary
            The graph that needs to be written to a data file.
        k : int
            The number of colors that is being tested for the chromatic number.
            This is used to number the nodes in the new graph file.
    Returns:
    --------
        None
    """
    # Convert graph to form that can be stored in a data file
    output_lines = ["Clique Problem:\n", f"{len(graph)}\n"]
    for node, neighbors in graph.items():
        file_node = (int(str(node).split("-")[0]) * k) - (k - (int(str(node).split("-")[1])))
        for neighbor in neighbors:
            file_neighbor = (int(str(neighbor).split("-")[0]) * k) - (k - (int(str(neighbor).split("-")[1])))
            if file_node < file_neighbor:
                output_lines.append(f"{file_node} {file_neighbor} 0\n")
    output_lines.append("$\n")
    with open("intermediate.dat", "w") as f:
        f.writelines(output_lines)

def main():
    """
    The main function for the graph coloring to clique mapping. This function
    will take a graph that we are attempting to find the chromatic number for
    and then map it to the clique problem. By solving the clique problem for
    the resulting graph, we can then determine the chromatic number for the
    graph coloring problem.
    """
    k = int(sys.argv[3])
    G = graph_util.read_graph_from_file(sys.argv[1])
    H = graph_coloring_to_clique(G, k)
    write_to_file(H, k)
    if sys.argv[2] == 'y':
        coloring = {key: 0 for key in H}
        graph_util.create_graph(H, coloring)
    return

if __name__ == "__main__":
    main()
