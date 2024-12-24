import heapq

def search_dijkstra(graph,start,end):
  queue = []
  heapq.heappush(queue,(0,start))
  distance = {x:float('inf') for x in graph}
  distance[start] = 0
  visited = set()
  parent = {start:-1}
  path=[]

  while queue:
    current_distance, current_node = heapq.heappop(queue)


    if current_node in visited:
      continue
    
    visited.add(current_node)
    
    if current_node == end:
      break
    
    for neighbour,weight in graph[current_node].items():
      temp = weight+current_distance
      if temp<distance[neighbour]:
        distance[neighbour] = temp
        heapq.heappush(queue,(temp,neighbour))
        parent[neighbour] = current_node

  node = end
  while node != -1:
    path.append(node)
    node = parent.get(node)
  path.reverse()
  return path,distance[end]





graph = {
  '0':{'1':4,'7':8},
  '1':{'0':4,'7':11,'2':8},
  '7':{'0':8,'1':11,'8':7,'6':1},
  '6':{'7':1,'8':6,'5':2},
  '8':{'7':7,'6':6,'2':2},
  '5':{'6':2,'2':4,'3':14,'4':10},
  '2':{'1':8,'8':2,'5':4,'3':7},
  '3':{'2':7,'4':9,'5':14},
  '4':{'3':9,'5':10}
}


start = '0'
end = '4'


parent,cost = search_dijkstra(graph,start,end)
print(parent,"\n")
print(cost)