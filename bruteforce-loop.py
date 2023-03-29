from itertools import product
import sys


# Function to check if a given coloring is valid for the graph
def is_valid_coloring_loop(coloring, graph):
    # Iterate through all vertices and their neighbors in the graph
    for vertex, neighbors in graph.items():
        # Check if the current vertex has the same color as any of its neighbors
        for neighbor in neighbors:
            if coloring[vertex] == coloring[neighbor]:
                # If it does, the coloring is not valid, so return False
                return False
    # If no conflicts are found, the coloring is valid, so return True
    return True

# Function to find a valid coloring for the graph using the given number of colors
def graph_coloring_loop(graph, num_colors):
    num_vertices = len(graph)
    # Generate all possible color combinations for the given number of colors
    for coloring in product(range(1, num_colors + 1), repeat=num_vertices):
        # Check if the current coloring is valid for the graph
        if is_valid_coloring_loop(coloring, graph):
            # If it is, return the coloring
            return coloring
    # If no valid coloring is found, return None
    return None

# Function to find the chromatic number of the graph using the brute force loop-based method
def find_chromatic_number_bruteforce_loop(graph):
    num_vertices = len(graph)
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
    graph = {}
    # Get the file name that was passed in as an argument
    file_name  = sys.argv[1]
    # Open the specifed file in order to read its data
    with open(file_name, 'r') as file:
        # Number of vertices should be the first line in the file
        num_vertices = int(file.readline())
        # Read each line in one by one and add each node to the list of neigbors
        # as necessary
        for line in file:
            if line[0] == '$':
                # Break condtion encountered, no more data remains
                break
            else:
                data = line.split(" ")
                node1 = int(data[0]) - 1
                node2 = int(data[1]) - 1
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
        print(graph)

    chromatic_number, coloring = find_chromatic_number_bruteforce_loop(graph)
    print(f"Chromatic number: {chromatic_number}")
    print(f"Coloring: {coloring}")

if __name__ == "__main__":
    main()
