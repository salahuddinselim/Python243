import heapq

def find_path(parent, end):
    path = []
    x = end
    while x != -1:
        path.append(x)
        x = parent.get(x)
    path.reverse()
    return path

def heuristic_value(node, goal):
    
    heuristic_map = {
        'A': {'D': 7},
        'B': {'D': 6}, 
        'C': {'D': 2},
        'D': {'D': 0}
    }
    return heuristic_map.get(node, {}).get(goal, 0)

def a_starSearch(graph, start, end):
    if start not in graph or end not in graph:
        return None, float('inf')

    pq = []
    heapq.heappush(pq, (0, start))
    distance = {x: float('inf') for x in graph}
    distance[start] = 0
    parent = {start: -1}
    f_heu = {x: float('inf') for x in graph}
    f_heu[start] = heuristic_value(start, end)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        
        if current_node == end:
            return find_path(parent, end), distance[end]

        
        for neighbor, weight in graph[current_node].items():
            temp = distance[current_node] + weight
            if temp < distance[neighbor]: 
                distance[neighbor] = temp
                f_heu[neighbor] = temp + heuristic_value(neighbor, end)
                parent[neighbor] = current_node
                heapq.heappush(pq, (f_heu[neighbor], neighbor))

    return None, float('inf') 


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}
start = 'A'
end = 'D'

path, cost = a_starSearch(graph, start, end)
print(f"\nShortest path is: {path}\n")
print(f"Total distance is: {cost}\n")
