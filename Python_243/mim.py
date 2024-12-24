import heapq
from math import sqrt


def heuristic(node, goal):
    return sqrt((coords[node][0] - coords[goal][0]) ** 2 + (coords[node][1] - coords[goal][1]) ** 2)


def find_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    return path[::-1]

def a_star_search(start, goal):
    pq = []  
    heapq.heappush(pq, (0, start))  
    g_cost = {start: 0}
    parent = {start: None}
    
    while pq:
        f, current = heapq.heappop(pq)
        
        if current == goal:  
            return find_path(parent, start, goal), g_cost[goal]
        
        for neighbor, edge_cost in adjlist[current]:
            temp_g = g_cost[current] + edge_cost
            if neighbor not in g_cost or temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f_cost = temp_g + heuristic(neighbor, goal)
                parent[neighbor] = current
                heapq.heappush(pq, (f_cost, neighbor))
    
    return None, float('inf')  


print("Enter number of vertices:")
V = int(input())
coords = {}
for _ in range(V):
    node, x, y = input().split()
    coords[node] = (int(x), int(y))

print("Enter number of edges:")
E = int(input())
adjlist = {}
for _ in range(E):
    node1, node2, cost = input().split()
    cost = int(cost)
    if node1 not in adjlist:
        adjlist[node1] = []
    if node2 not in adjlist:
        adjlist[node2] = []
    adjlist[node1].append((node2, cost))
    adjlist[node2].append((node1, cost))  

print("Enter start and goal nodes:")
start, goal = input().split()


path, cost = a_star_search(start, goal)
if path:
    print(f"Solution path: {path}")
    print(f"Solution cost: {cost}")
else:
    print("No path found")
