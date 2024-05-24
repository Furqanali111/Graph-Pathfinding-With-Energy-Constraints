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



def relaxed_dijkstra(graph, source, target):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0
    queue = [(0, source)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == target:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = predecessors[current_node]
            return path

        if current_distance > distances[current_node]:
            continue

        for neighbor_node in graph[current_node]:
            distance = current_distance + Dist.get(f"{current_node},{neighbor_node}", float('inf'))
            if distance < distances[neighbor_node]:
                distances[neighbor_node] = distance
                predecessors[neighbor_node] = current_node
                heapq.heappush(queue, (distance, neighbor_node))
    return []

if __name__ == "__main__":
    # Replace with the actual source and target nodes
    source = '1'  # Replace with your source node
    target = '50'  # Replace with your target node

    # Call the relaxed Dijkstra algorithm to find the shortest path
    shortest_path = relaxed_dijkstra(G, source, target)

    if not shortest_path:
        print("No path found from source to target.")
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

        # Calculate the total energy cost (assuming it's in the 'Cost' dictionary)
        total_energy_cost = 0
        for i in range(len(shortest_path) - 1):
            from_node, to_node = shortest_path[i], shortest_path[i + 1]
            edge_energy_cost = Cost.get(f"{from_node},{to_node}", 0)  # Assuming 0 if not found
            total_energy_cost += edge_energy_cost

        print("Total energy cost:", total_energy_cost)