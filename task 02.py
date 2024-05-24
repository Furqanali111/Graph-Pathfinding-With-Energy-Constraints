import json
import heapq

# Load graph data from JSON files
with open('G.json', 'r') as g_file:
     G = json.load(g_file)
with open('Coord.json', 'r') as coord_file:
     Coord = json.load(coord_file)
with open('Dist.json', 'r') as dist_file:
     Dist = json.load(dist_file)
with open('Cost.json', 'r') as cost_file:
     Cost = json.load(cost_file)


# Define the UCS function with an energy budget
def ucs_with_energy(graph, source, target, energy_budget):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0
    queue = [(0, source, 0)]

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
            neighbor_node = neighbor
            edge_distance = Dist.get(f"{current_node},{neighbor_node}", float('inf'))
            distance = current_distance + edge_distance
            energy_cost = current_energy + Cost.get(f"{current_node},{neighbor_node}", 0)

            if distance < distances[neighbor_node] and energy_cost <= energy_budget:
                distances[neighbor_node] = distance
                predecessors[neighbor_node] = current_node
                heapq.heappush(queue, (distance, neighbor_node, energy_cost))
    return []

if __name__ == "__main__":
    source = '1'
    target = '50'
    energy_budget = 287932

    shortest_path = ucs_with_energy(G, source, target, energy_budget)

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