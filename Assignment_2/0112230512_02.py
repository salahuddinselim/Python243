import math
import random


#calculating the distance here
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


#calculating distance after using the route
def calculate_distance(route, location):
    return sum(euclidean_distance(location[route[i]], location[route[i + 1]]) for i in range(len(route) - 1))


#finding the route using this function 
def route_find(location):
    route = list(range(1, len(location)))
    random.shuffle(route)
    return [0] + route + [0]


#finding the neighbor from here. We have taken 2 random neighbor's and swaping them with each other
def find_neighbor(route):
    n1, n2 = random.sample(range(1, len(route) - 1), 2)
    neighbor = route[:]
    neighbor[n1], neighbor[n2] = neighbor[n2], neighbor[n1]
    return neighbor


''' 
    Here we are using the hill climbing methond to find the shortest path. 
    Hill climbing only use Heuristic value to find the shortest path. As it
    only use heuristic value it can't overcome the local minima and stack in 
    it as a result after some time it stops there. It also can't back track.

'''
def hill_climbing(location):
    current = route_find(location)
    current_distance = calculate_distance(current, location)
    while True:
        neighbors = [find_neighbor(current) for _ in range(100)]
        best_neighbor = min(neighbors, key=lambda x: calculate_distance(x, location))
        best_distance = calculate_distance(best_neighbor, location)
        if best_distance < current_distance:
            current, current_distance = best_neighbor, best_distance
        else:
            break
    return current, current_distance


'''
    Here we are using the hill climbing methond to find the shortest path. Hill climbing only use Heuristic
    value to find the shortest path and also using a random function to overcome the local minima.

'''
def simulated_annealing(location, temp, rate, max_it):
    current = route_find(location)
    current_distance = calculate_distance(current, location)
    new_temp = temp
    best_route, best_distance = current, current_distance
    for _ in range(max_it):
        neighbor = find_neighbor(current)
        neighbor_distance = calculate_distance(neighbor, location)
        del_E = neighbor_distance - current_distance
        if del_E < 0 or random.uniform(0, 1) < math.exp(-del_E / new_temp):
            current, current_distance = neighbor, neighbor_distance
            if current_distance < best_distance:
                best_distance, best_route = current_distance, current
        new_temp *= rate
        if new_temp < 1e-10:
            break
    return best_route, best_distance
'''
    Here we are taking values from user 
'''
def userInput():
    no = int(input("Enter number of locations: "))
    print("Enter the locations: ")
    location = []
    for i in range(no):
        x, y = map(float, input(f"Enter location {i + 1}: ").split())
        location.append((x, y))
    return location

def main():
    locations = userInput()
    hill_route, hill_distance = hill_climbing(locations)
    simu_route, simu_distance = simulated_annealing(locations, temp=100, rate=0.99, max_it=1000)
    print(f"Hill climbing route is {hill_route} and the distance is: {hill_distance}")
    print(f"Simulated Annealing route is {simu_route} and distance is: {simu_distance}")

if __name__ == "__main__":
    main()



'''
    Simulated Annealing route is [0, 1, 3, 4, 2, 0] and distance is: 14.67004637770997
    Hill climbing route is [0, 1, 3, 4, 2, 0] and the distance is: 14.67004637770997
    Both got the same value. But some time the hill climbing algorithm can stuck in the 
    local minima because it use greedy approach and don't track his path. So when it reach
    in a position where the next node is higher then it, it can't go through it and stack 
    there.
    But the simulated annealing can overcome this problem. As we are using both heuristic and 
    random function to overcome this. It is like the hill climbing approach but when get
    stuck in the local minima it use the random function to pass this phase. as a result 
    we can get a result. 

'''