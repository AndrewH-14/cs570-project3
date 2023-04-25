import sys
sys.path.append('../')
import heuristic
import bruteforce
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
        G[str(variable)]  = []
        G[('-' + str(variable))] = []
    # Create the True, False, and Base triangle
    G['T'] = ['F', 'B']
    G['F'] = ['B', 'T']
    G['B'] = ['T', 'F']

    # Add the edges between the variable nodes and their negations and the B node
    for variable in variables:
        G['B'].extend(str(variable))
        G['B'].extend([('-' + str(variable))])
        G[str(variable)].extend(['B', ('-' + str(variable))])
        G[('-' + str(variable))].extend(['B', str(variable)])

    # Add the OR-gadget graphs to G
    for i, clause in enumerate(formula):
        u, v, w = clause
        c0, c1, c2, c3, c4, c5 = f'c{i}_0', f'c{i}_1', f'c{i}_2', f'c{i}_3', f'c{i}_4', f'c{i}_5'
        # Create first OR gate
        G[str(u)].append(c0)
        G[str(v)].append(c1)
        G[str(w)].append(c4)
        G[c0] = [str(u), c1, c2]
        G[c1] = [str(v), c0, c2]
        G[c2] = [c0, c1, c3]
        G[c3] = [c2, c4, c5]
        G[c4] = [str(w), c3, c5]
        G[c5] = [c3, c4, 'B', 'F']
        G[c4] = [str(w), c3, c5]
        G['B'].append(c5)
        G['F'].append(c5)

    # Color the graph to determine if the formula is solvable
    k, coloring = bruteforce.find_chromatic_number_bruteforce_loop(G)

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
        print(f"Chromatic number: {k}")
        print(f"Coloring: {coloring}")
    else:
        print("Impossible")
    if sys.argv[2] == 'y':
        graph_util.create_graph(G, coloring)
    return

if __name__ == "__main__":
    main()
