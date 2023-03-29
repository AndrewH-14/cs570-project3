def is_valid_color(vertex, color):
    """
    Function that will check whether the vertex can be colored to the provided
    color.
    Parameters:
    -----------

    Returns:
    --------

    """
    return

def brute_force_coloring(graph, num_colors):
    """
    Function that will solve the graph coloring problem using a brute force
    method.
    Parameters:
    -----------
        graph : The graph that we are attempting to color.
    Returns:
    --------
        int : The chromatic number of the graph (minimum colors needed)
    """
    # Get the number of vertices in the graph
    num_vertices = len(graph)


def main():
    """
    Main function for the graph coloring brute force program.
    Parameters:
    -----------
        None
    Returns:
    --------
        None
    """
    graph_4_vertexes = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }

    # Start the brute force coloring algorithm
    min_solution = brute_force_coloring(graph)
    print("Minimum Solution: ", min_solution)

if __name__ == "__main__":
    main()
