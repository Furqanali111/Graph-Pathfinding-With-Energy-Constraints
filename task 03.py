import json
import heapq

# Load graph data from JSON files
with open('G.json', 'r') as g_file:
    G = json.load(g_file)
with open('Dist.json', 'r') as dist_file:
    Dist = json.load(dist_file)
with open('Cost.json', 'r') as cost_file:
    Cost = json.load(cost_file)
with open('Coord.json', 'r') as coord_file:
    Coord = json.load(coord_file)
# Define the A* search function with an energy budget
    def astar_with_energy(graph, source, target, energy_budget):
        distances = {node: float('inf') for node in graph}
        predecessors = {node: None for node in graph}
        distances[source] = 0
        queue = [(0, source, 0)]  # Tuple structure: (current distance, current node, current energy)

        while queue:
            current_distance, current_node, current_energy = heapq.heappop(queue)

            if current_node == target:
                path = []
                while current_node is not None:
                    path.insert(0, current_node)
                    current_node = predecessors[current_node]
                return path

            if current_distance > distances[current_node] or current_energy > energy_budget:
                continue

            for neighbor in graph.get(current_node, []):
                neighbor_node = neighbor  # Adapt this to your specific data structure
                edge_distance = Dist.get(f"{current_node},{neighbor_node}", float('inf'))  # Adapt this to your specific data structure
                energy_cost = Cost.get(f"{current_node},{neighbor_node}", 0)  # Adapt this to your specific data structure

                if energy_cost + current_energy > energy_budget:
                    continue  # Skip neighbors that exceed the energy budget

                distance = current_distance + edge_distance  # Adapt this to your specific data structure
                total_cost = distance + estimate_remaining_energy(neighbor_node, target, energy_budget)

                if total_cost < distances[neighbor_node]:
                    distances[neighbor_node] = total_cost
                    predecessors[neighbor_node] = current_node
                    heapq.heappush(queue, (total_cost, neighbor_node, current_energy + energy_cost))

        return []

    # Define the heuristic function
    def estimate_remaining_energy(node, target, energy_budget):
        # This heuristic function estimates the remaining energy required to reach the target node
        # You can modify this function based on your specific problem and data
        # A simple example is to use a straight-line distance as the heuristic (assuming no energy costs)
        return straight_line_distance(node, target)

    def straight_line_distance(node1, node2):
        # Calculate the straight-line Euclidean distance between two nodes (ignoring energy costs)
        coord1 = Coord.get(node1, (0, 0))
        coord2 = Coord.get(node2, (0, 0))
        x1, y1 = coord1
        x2, y2 = coord2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if __name__ == "__main__":
    source = '1'
    target = '50'
    energy_budget = 287932

    shortest_path = astar_with_energy(G, source, target, energy_budget)

    if not shortest_path:
        print("No path found from source to target within the energy budget.")
    else:
        # Print the shortest path
        print("Shortest path:", '->'.join(shortest_path))

        # Calculate the total distance
        total_distance = 0
        for i in range(len(shortest_path) - 1):
            from_node, to_node = shortest_path[i], shortest_path[i + 1]
            edge_distance = Dist.get(f"{from_node},{to_node}", float('inf'))
            total_distance += edge_distance

        print("Shortest distance:", total_distance)

        # Calculate the total energy cost (within the budget)
        total_energy_cost = 0
        for i in range(len(shortest_path) - 1):
            from_node, to_node = shortest_path[i], shortest_path[i + 1]
            edge_energy_cost = Cost.get(f"{from_node},{to_node}", 0)
            total_energy_cost += edge_energy_cost

        print("Total energy cost:", total_energy_cost)
