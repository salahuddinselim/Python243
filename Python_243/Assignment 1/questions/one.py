import heapq
from math import sqrt

def heuristic_value(node,goal):
  calculate = sqrt((node[0]-goal[0])**2 + (node[1]-goal[1])**2)
  return calculate



def find_path(parent,goal):
  path = []
  node = goal
  while node != -1:
    path.append(node)
    node = parent.get(node)
  return path[::-1]



def a_star_search(arr,start,goal):
  if arr[start[0]][start[1]] == 1 and arr[goal[0]][goal[1]] == 1:
    return None , float('inf')
  pq = []
  heapq.heappush(pq,(0,start))
  distance = {start:0}
  parent = {start:-1}
  cost = {start: heuristic_value(start,goal)}
  while pq:
    current_distance, current_node = heapq.heappop(pq)
    if current_node == goal:
      return find_path(parent,goal),distance[goal]
    for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
      neighbour = (current_node[0]+x,current_node[1]+y)
      if 0<=neighbour[0]<row and 0<=neighbour[1]<col and arr[neighbour[0]][neighbour[1]]==0:
        temp = distance[current_node] + 1
        if neighbour not in distance or temp < distance[neighbour]:
          distance[neighbour] = temp
          cost[neighbour] = temp + heuristic_value(neighbour,goal)
          parent[neighbour] = current_node
          heapq.heappush(pq,(cost[neighbour],neighbour))
  return None, float('inf')




print("Enter number of row and column: ")
row,col = map(int,input().split())
arr = [list(map(int,input().split())) for x in range(row)]
print("Enter the start point: ")
start = tuple(map(int,input().split()))
print("Enter the goal point: ")
goal = tuple(map(int,input().split()))

find,cost = a_star_search(arr,start,goal)
print(f"\nTotal cost is : {cost}\n")
print(f"Path is : {find}\n")
