# Function to check if the color can be assigned to the vertex without violating the constraint
def is_valid_coloring(vertex, color, graph, vertex_colors):
    for neighbor in graph[vertex]:
        # If the neighbor vertex has the same color, return False (not valid)
        if vertex_colors[neighbor] == color:
            return False
    # If no neighbor vertices have the same color, return True (valid)
    return True

# Recursive function to perform graph coloring using backtracking
def graph_coloring(graph, num_colors, vertex_colors, current_vertex):
    # Base case: If all vertices are colored, return the current coloring
    if current_vertex == len(graph):
        return vertex_colors

    # Iterate through possible colors for the current vertex
    for color in range(1, num_colors + 1):
        # If the color is valid, assign it to the current vertex
        if is_valid_coloring(current_vertex, color, graph, vertex_colors):
            vertex_colors[current_vertex] = color

            # Recursively move on to the next vertex
            result = graph_coloring(graph, num_colors, vertex_colors, current_vertex + 1)

            # If a valid coloring is found, return it
            if result:
                return result

            # Backtrack and uncolor the current vertex
            vertex_colors[current_vertex] = 0

    # If no valid coloring is found, return None
    return None

# Function to find the chromatic number of the graph using the brute force method
def find_chromatic_number_bruteforce(graph):
    num_vertices = len(graph)
    # Iterate through possible numbers of colors, starting from 1
    for num_colors in range(1, num_vertices + 1):
        # Initialize the vertex_colors array with zeros (uncolored vertices)
        vertex_colors = [0] * num_vertices
        # Try to color the graph with the current number of colors
        coloring = graph_coloring(graph, num_colors, vertex_colors, 0)

        # If a valid coloring is found, return the chromatic number and coloring
        if coloring:
            return num_colors, coloring

    # If no valid coloring is found, return None
    return None

# Usage
graph = {
    0: [1, 2, 3],
    1: [0, 2, 4],
    2: [0, 1, 3, 4],
    3: [0, 2, 4],
    4: [1, 2, 3]
}

graph_8_nodes = {
    0: [1, 2, 4],
    1: [0, 3, 5],
    2: [0, 3, 6],
    3: [1, 2, 7],
    4: [0, 5, 6],
    5: [1, 4, 7],
    6: [2, 4, 7],
    7: [3, 5, 6],
}

graph_15_nodes = {
    0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    1: [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    2: [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    3: [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    4: [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    5: [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    6: [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14],
    7: [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14],
    8: [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14],
    9: [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14],
    10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14],
    11: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14],
    12: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14],
    13: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14],
    14: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
}

chromatic_number, coloring = find_chromatic_number_bruteforce(graph_8_nodes)
print(f"Chromatic number: {chromatic_number}")
print(f"Coloring: {coloring}")
