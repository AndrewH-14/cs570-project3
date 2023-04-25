"""
Program that will solve the graph coloring problem using the provided graph as
input.

Written by: Andrew Hankins

Running the program:
python3 bruteforce.py <data file> <y/n diagram>
"""
from itertools import product
import sys
import graph_util

def is_valid_coloring_loop(coloring, graph):
    """
    Checks to see if the graph/coloring pair is a valid solution to the graph
    coloring problem.
    Parameters:
    -----------
        coloring : dictionary
            The coloring of the graph.
        graph : dictionary
            The graph that is being colored.
    Returns:
    --------
        bool : Whether or not the graph is a valid solution to the graph
               coloring problem.
    """
    # Iterate through all vertices and their neighbors in the graphs
    for vertex, neighbors in graph.items():
        # Check if the current vertex has the same color as any of its neighbors
        for neighbor in neighbors:
            if coloring[vertex] == coloring[neighbor]:
                # If it does, the coloring is not valid, so return False
                return False
    # If no conflicts are found, the coloring is valid, so return True
    return True

def graph_coloring_loop(graph, num_colors):
    """
    Function that will check all possible combinations with the number of colors
    provided in order to find a valid solution.
    Parameters:
    -----------
        graph : dictionary
            The graph that we are attempting to find a coloring for.
        num_colors : int
            The number of colors that are allowed.
    Returns:
    --------
        dictionary : The coloring of the graph is one is found. Will be None if
                     no possible valid colorings exist.
    """
    num_vertices = len(graph.keys())
    # Generate all possible color combinations for the given number of colors
    for coloring in product(range(1, num_colors + 1), repeat=num_vertices):
        # Create the coloring dictionary
        coloring_dict = dict(zip(dict(sorted(graph.items())).keys(), coloring))
        # Check if the current coloring is valid for the graph
        if is_valid_coloring_loop(coloring_dict, graph):
            # If it is, return the coloring
            return coloring_dict
    # If no valid coloring is found, return None
    return None

def find_chromatic_number_bruteforce_loop(graph):
    """
    Function that will attempt to solve the graph coloring problem with the
    smallest possible number of colors.
    Parameters:
    -----------
        graph : dictionary
            The graph that we are attempting to find the chromatic number for.
    Returns:
    --------
        int : Minumum number of colors able to color the graph.
        dictionary : A dictionary of the graph coloring.
    """
    num_vertices = len(graph.keys())
    # Iterate through possible numbers of colors, starting from 1
    for num_colors in range(1, num_vertices + 1):
        # Try to color the graph with the current number of colors
        coloring = graph_coloring_loop(graph, num_colors)
        # If a valid coloring is found, return the chromatic number and coloring
        if coloring:
            return num_colors, coloring
    # If no valid coloring is found, return None
    return None

def main():
    """
    The main function for the program.
    """
    # Read graph from the data file
    graph = graph_util.read_graph_from_file(sys.argv[1])
    # Determine the chromatic coloring of the graph using the bruteforce method.
    chromatic_number, coloring = find_chromatic_number_bruteforce_loop(graph)
    # Print off the resulting information
    print(f"Chromatic number: {chromatic_number}")
    print(f"Coloring: {coloring}")
    # Provide a diagram of the graph if requested
    if sys.argv[2] == 'y':
        graph_util.create_graph(graph, coloring)

if __name__ == "__main__":
    main()
