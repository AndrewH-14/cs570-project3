"""
Program that will solve the map the maximum independent set problem to the
graph coloring problem.

Written by: Andrew Hankins

Running the program:
python3 max_independent_set.py <graph file>
"""
import sys
import networkx as nx
import matplotlib.pyplot as plt

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

def independent_set_to_graph_coloring(graph):
    """
    """
    new_graph = {}

    for vertex in graph:
        # Create a list of all other vertices in the graph
        arr_vertices = []
        for i in range(1, len(graph)+1):
            if not i == vertex:
                arr_vertices.append(i)
        # If the vertex is a neighbor, remove it from the list. At the end, the
        # array will include all vertices that the vertex is not adjacent to.
        for neighbor in graph[vertex]:
            if neighbor in arr_vertices:
                arr_vertices.remove(neighbor)
        # Add the non adjacent vertices as neighbors in the new graph
        for new_neighbor in arr_vertices:
            if vertex in new_graph:
                if new_neighbor not in new_graph[vertex]:
                    new_graph[vertex].append(new_neighbor)
            else:
                new_graph[vertex] = [new_neighbor]
            if new_neighbor in new_graph:
                if vertex not in new_graph[new_neighbor]:
                    new_graph[new_neighbor].append(vertex)
            else:
                new_graph[new_neighbor] = [vertex]

    return new_graph

def write_to_file(graph):
    """
    """
    output_lines = [f"{len(graph)}\n"]
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if node < neighbor:
                output_lines.append(f"{node} {neighbor} 0\n")
    output_lines.append("$\n")
    with open("intermediate.txt", "w") as f:
        f.writelines(output_lines)


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

    new_graph = independent_set_to_graph_coloring(graph)
    write_to_file(new_graph)

    return

if __name__ == "__main__":
    main()
