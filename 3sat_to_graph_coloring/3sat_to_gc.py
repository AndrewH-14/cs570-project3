import sys
sys.path.append('../')
import heuristic
import graph_util

def sat_to_3coloring(formula):
    # Parse the SAT formula to extract the variables and clauses
    variables = set()
    for clause in formula:
        variables |= set(abs(literal) for literal in clause)

    # Graph that we will color
    G = {}
    # For every variable and variable negation, construct a vertex in the graph
    for variable in variables:
        G[variable]  = []
        G[-variable] = []
    # Create the True, False, and Base triangle
    G['T'] = ['F', 'B']
    G['F'] = ['B', 'T']
    G['B'] = ['T', 'F']

    # Add the edges between the variable nodes and their negations and the B node
    G['B'].extend(variables)
    for variable in variables:
        G[variable].extend(['B', -variable])
        G[-variable].extend(['B', variable])

    # Add the OR-gadget graphs to G
    for i, clause in enumerate(formula):
        u, v, w = clause
        G[f'c{i}_1'] = [u, f'c{i}_4', f'c{i}_5']
        G[u].append(f'c{i}_1')
        G[f'c{i}_2'] = [v, f'c{i}_4', f'c{i}_5']
        G[v].append(f'c{i}_2')
        G[f'c{i}_3'] = [w, f'c{i}_4', f'c{i}_5']
        G[w].append(f'c{i}_3')
        G[f'c{i}_4'] = ['F', 'B']
        G['F'].append(f'c{i}_4')
        G['B'].append(f'c{i}_4')
        G[f'c{i}_5'] = ['F', 'B']
        G['F'].append(f'c{i}_5')
        G['B'].append(f'c{i}_5')
        G[f'c{i}_4'].extend([f'c{i}_1', f'c{i}_2', f'c{i}_3'])
        G[f'c{i}_5'].extend([f'c{i}_1', f'c{i}_2', f'c{i}_3'])

    # Color the graph to determine if the formula is solvable
    k, coloring = heuristic.heuristic_search(G)

    return (True if k <= 3 else False), G, k, coloring

def read_file(file_name):
    # Read the entire file as a string
    with open(file_name, 'r') as f:
        lines = f.readlines()
    # Remove any leading or trailing whitespace
    lines = [line.split() for line in lines]
    # Remove the first line which contains the problem type
    lines.pop(0)
    # Remove any lines that are empty
    lines = [line for line in lines if line]
    # Split each line into a list of inegers representing literals in clause
    clauses = []
    for line in lines:
        if '$' in line:
            break
        literals = [int(x) for x in line]
        clauses.append(literals)
    return clauses

def main():
    sat_formula = read_file(sys.argv[1])
    solvable, G, k, coloring = sat_to_3coloring(sat_formula)
    if solvable:
        print("Possible!")
    else:
        print("Impossible")
    if sys.argv[2] == 'y':
        graph_util.create_graph(G, coloring)
    return

if __name__ == "__main__":
    main()
