# Graph-Pathfinding-With-Energy-Constraints
This repository contains three different Python scripts implementing various pathfinding algorithms within a weighted graph with additional energy constraints. The algorithms covered are relaxed Dijkstra's algorithm, Uniform Cost Search (UCS) with energy constraints, and A* search with energy constraints. These scripts are designed to find the shortest path between two nodes in a graph while considering distance and energy budget constraints.

# Repository Structure
G.json: Contains the graph data represented as an adjacency list.
Dist.json: Stores the distances between nodes in the graph.
Cost.json: Stores the energy cost required to traverse between nodes.
Coord.json: Contains the coordinates of the nodes used for heuristic calculations.

# Scripts
1) Task01.py
Description: Implements the relaxed Dijkstra's algorithm to find the shortest path between two nodes based on distance.
2) Task02.py
Description: Implements Uniform Cost Search (UCS) that considers both distance and energy constraints to find the shortest path between two nodes.
3) Task03.py
Description: Implements the A* search algorithm with energy constraints, using a heuristic based on straight-line distance.

# Main Script
main.py
Description: A main script to choose between the three tasks interactively.
