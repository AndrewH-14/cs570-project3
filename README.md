# NP-Complete Project: Graph Coloring
**Name:** Andrew Hankins
**Course:** CS 570
**Due:** May 7th, 2023

## Requirements

The programs in this repository have been tested and developed on `Python 3.10.6`.

In order to run the graph coloring programs, you will need to install the following Python packages:
* `networkx version 2.5.1`: This package us used for creating and manipulating graphs. It provides a simple and powerful interface for working with graphs in Python, including algorithms for graph traversal, shortest paths, and more.
* `matplotlib version 3.4.3`: This package is used for plotting graphs. It provides a wide range of plotting tools and customization options.

To install each of these packages, you can used the `pip` package manager. Use the following commands to install them:
```
pip install networkx==2.5.1
pip install matplotlib==3.4.2
```

## Repository Structure
```
CS570-Project3/
 ├── README.md : TODO
 ├── heuristic.py : TODO
 ├── bruteforce.py : TODO
 ├── optimal/
 |     ├── graph.txt : TODO
 |     ├── graph2.txt : TODO
 |     ├── graph3.txt : TODO
 |     ├── ...
 |     ├── graph10.txt : TODO
 |
 ├── suboptimal/
 |    ├── graph.txt : TODO
 |    ├── graph2.txt : TODO
 |
 ├── max_independent_set/
 |    ├── max_independent_set.py : TODO
 |    ├── run_mapping.sh
 |
 ├── clique/
 |    ├── clique_problem.py : TODO
```

## Brute Force Algorithm

**Approach:**
For the brute force graph coloring algorithm, the program will incrementally test all possible graph colorings from 1 ... k. The program will exit as soon as the first solution is found, which is gaurantted to be the chromatic number, or least number of colors needed to color the graph.

**Running the brute force algorithm:**
In order to run the brute force algorithm for the graph coloring problem, use the following command:
```
python3 bruteforce.py <graph> <visual>
```
The `<graph>` arguments corresponds to a graph data file that follows the following format:
```
<num vertices>
<vertex 1> <vertex 2> <weight>
<vertex 3> <vertex 1> <weight>
...
<vertex 4> <vertex 2> <weigth>
$
```
Ex:
```
3
1 2 1
1 3 1
2 3 1
$
```
The `<visual>` argument requires a `y` or `n` option. If `y` is given, the networkx library will be used to create a visual representation of the graph coloring.

## Heuristic Algorithm

**Approach:**
The heuristic algorithm used for the graph coloring problem works by incrementally attempting to color the graph in decreasing order of the node's degree. This means that nodes with more edges connected to them will be colored first, as they are more likely to cause conflicts if left uncolored. If the current number of colors is not enough to color the graph without conflicts, the algorithm will increase the number of colors allowed. This continues until a valid coloring is found.

**Running the heuristic algorithm:**
```
python3 heuristic.py <graph> <visual>
```

**Problems with the heuritic approach:**
Since the heurstic approach attempts to guess at the optimal solution, it can sometimes provide suboptimal solutions for certain graphs. One of these graphs is the following:
```
8
1 2 1
2 3 1
3 4 1
4 5 1
5 6 1
6 1 1
1 7 1
4 8 1
$
```

## Mapping to the Graph Coloring Problem

### Independent Set

**Running the mapping:**

## Mapping the Graph Coloring Problem to other NP-Complete Problems

### Clique Problem

**Running the mapping:**

## References
The following references were used when create the graph coloring algorithms and mappings:
```
1. https://www.researchgate.net/publication/305457929_Reducing_graph_coloring_to_clique_search
```
