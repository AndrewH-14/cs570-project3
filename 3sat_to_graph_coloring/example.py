def sat_to_3coloring(sat_formula):
    # Parse the SAT formula to extract the variables and clauses
    variables = set()
    clauses = []
    for clause in sat_formula:
        variables |= set(abs(literal) for literal in clause)
        clauses.append(set(clause))

    # Create the graph G
    G = {}

    # Add the variable nodes and their negations to G
    for variable in variables:
        G[variable] = set()
        G[-variable] = set()

    # Add the additional nodes T, F, B to G
    G['T'] = set()
    G['F'] = set()
    G['B'] = set()

    # Add the edges between T, F, B to form a triangle
    G['T'].add('F')
    G['F'].add('B')
    G['B'].add('T')

    # Add the edges between the variable nodes and their negations and the B node
    for variable in variables:
        G[variable].add('B')
        G[-variable].add('B')

    # Add the OR-gadget graphs to G
    for i, clause in enumerate(clauses):
        u, v, w = clause
        G[f'c{i}_1'] = [u]
        G[f'c{i}_2'] = [v]
        G[f'c{i}_3'] = [w]
        G[f'c{i}_4'] = ['F', 'B']
        G[f'c{i}_5'] = ['F', 'B']
        G[u].append(f'c{i}_1')
        G[v].append(f'c{i}_2')
        G[w].append(f'c{i}_3')
        G[f'c{i}_4'].update([f'c{i}_1', f'c{i}_2', f'c{i}_3'])
        G[f'c{i}_5'].update([f'c{i}_1', f'c{i}_2', f'c{i}_3'])

    # Run the 3-coloring algorithm on G
    k_coloring = greedy_coloring(G)

    # Check if G can be 3-colored
    if len(set(k_coloring.values())) > 3:
        return None

    # Map the colors to True, False, and Base
    true_variables = set(variable for variable in variables if k_coloring[variable] == 1)
    false_variables = set(variable for variable in variables if k_coloring[variable] == 2)
    base_variables = set(variable for variable in variables if k_coloring[variable] == 3)

    # Construct the satisfying assignment
    satisfying_assignment = {}
    for variable in true_variables:
        satisfying_assignment[variable] = True
    for variable in false_variables:
        satisfying_assignment[variable] = False
    for variable in base_variables:
        satisfying_assignment[variable] = None

    return satisfying_assignment

def greedy_coloring(G):
    # Initialize the color of each vertex to None
    vertex_colors = {vertex: None for vertex in G}

    # Color the vertices greedily
    for vertex in sorted(G, key=lambda x: len(G[x]), reverse=True):
        available_colors = set(range(1, len(G) + 1))
        for neighbor in G[vertex]:
            if vertex_colors[neighbor] in available_colors:
                available_colors.remove(vertex_colors[neighbor])
        vertex_colors[vertex] = min(available_colors)

    return vertex_colors
