def hill_climbing(maze, start, goal, max_it):
    def heuristic(pos):
        return abs(goal[1] - pos[1]) + abs(goal[0] - pos[0])

    def find_neighbor(pos):
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        neighbor = []
        for move in moves:
            new_x = pos[0] + move[0]
            new_y = pos[1] + move[1]
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0:
                neighbor.append((new_x, new_y))
        return neighbor

    current_pos = start
    current_path = [current_pos]

    for _ in range(max_it):
        if current_pos == goal:
            return "Path Found", current_path

        neighbor = find_neighbor(current_pos)
        if not neighbor:
            return "Dead end", current_path

        next_pos = min(neighbor, key=heuristic)
        if heuristic(current_pos) < heuristic(next_pos):
            return "Dead End", current_path

        current_pos = next_pos
        current_path.append(current_pos)

    return "Path Not Found", current_path

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)

max_it = 100
message, path = hill_climbing(maze, start, goal, max_it)
print(path)
print("\n", message)
