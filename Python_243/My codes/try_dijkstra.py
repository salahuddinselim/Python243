import heapq


def dijkstra(graph, strat, goal):
  pq=[]
  heapq.heappush(pq,(0,strat))
  distance = {x:float('inf') for x in graph}
  parent = set()
  visited=list()
  path = {strat:-1}
  distance[strat] = 0
  while pq:
    current_distance, current_node = heapq.heappop(pq)
    if current_node in visited:
      continue
    if current_node == goal:
      break
    for neighbour, weight in graph[current_node].items():
      temp_distance = weight+current_distance
      if temp_distance<distance[neighbour]:
        distance[neighbour] = temp_distance
        parent[neighbour] = current_node
        heapq.heappush(pq(temp_distance,neighbour))
  node = goal
  while node != -1:
    path.append(node)
    node = parent.get(node)
  path.reverse()
  return path,distance[goal]
