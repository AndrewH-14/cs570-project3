"""
"""
import sys
sys.path.append('../')
import graph_util


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
    G = graph_util.read_graph_from_file(file_name)
    H = graph_coloring_to_clique(G, k)
    write_to_file(H, k)
    if visual == 'y':
        coloring = {key: 0 for key in H}
        graph_util.create_graph(H, coloring)
    return

if __name__ == "__main__":
    main()
