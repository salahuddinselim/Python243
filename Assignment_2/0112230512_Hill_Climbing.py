import math
import random

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_distance(route, location):
    return sum(euclidean_distance(location[route[i]], location[route[i + 1]]) for i in range(len(route) - 1))

def route_find(location):
    route = list(range(1, len(location)))
    random.shuffle(route)
    return [0] + route + [0]

def find_neighbor(route):
    n1, n2 = random.sample(range(1, len(route) - 1), 2)
    neighbor = route[:]
    neighbor[n1], neighbor[n2] = neighbor[n2], neighbor[n1]
    return neighbor

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
    print(f"Hill climbing route is {hill_route} and the distance is: {hill_distance}")

if __name__ == "__main__":
    main()
