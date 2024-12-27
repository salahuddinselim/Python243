# Dijkstra's Algorithm
import heapq

def dijkstra(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# A* Algorithm
def a_star(graph, start, goal, heuristic_function):
    pq = []
    heapq.heappush(pq, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    f_costs = {node: float('inf') for node in graph}
    f_costs[start] = heuristic_function(start, goal)
    came_from = {}

    while pq:
        _, current_node = heapq.heappop(pq)

        if current_node == goal:
            return reconstruct_path(came_from, current_node), distances[goal]

        for neighbor, weight in graph[current_node].items():
            tentative_distance = distances[current_node] + weight
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                f_costs[neighbor] = tentative_distance + heuristic_function(neighbor, goal)
                came_from[neighbor] = current_node
                heapq.heappush(pq, (f_costs[neighbor], neighbor))

    return None, float('inf')

def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    path.reverse()
    return path

def heuristic_function(node, goal):
    heuristic_map = {
        'A': {'D': 7},
        'B': {'D': 6},
        'C': {'D': 2},
        'D': {'D': 0}
    }
    return heuristic_map.get(node, {}).get(goal, 0)

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

# Test Dijkstra
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")

# Test A*
goal_node = 'D'
shortest_path, cost = a_star(graph, start_node, goal_node, heuristic_function)
print(f"Shortest path from {start_node} to {goal_node}: {shortest_path}")
print(f"Cost of the path: {cost}")