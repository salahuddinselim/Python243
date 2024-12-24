import heapq


def Dijkstra(graph,start):
  pq=[]
  heapq.heappush(pq,(0,start))
  distance = {x:float('inf') for x in graph}
  distance[start] = 0
  visited = set()
  parent = list()
  
  while pq:
    current_distance,current_node = heapq.heappop(pq)
    if current_node in visited:
      continue
    else:
      visited.add(current_node)
    for neighbour , weight in graph[current_node].items():
      temp_distance=current_distance+weight
      if temp_distance<distance[neighbour]:
        distance[neighbour] = temp_distance
        heapq.heappush(pq,(distance[neighbour],neighbour))

  return distance

graph = {
  'A':{'B':1, 'C':4},
  'B':{'A':1, 'C':2,'D':6},
  'C':{'A':4,'B':2,'D':3},
  'D':{'B':6,'C': 3}
}
start = 'A'

distances = Dijkstra(graph,start)
print(distances)
