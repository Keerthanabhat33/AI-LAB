import heapq

GOAL_STATE = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]  


goal_positions = {}
for i in range(3):
    for j in range(3):
        goal_positions[GOAL_STATE[i][j]] = (i, j)

def h_manhattan_distance(state):
    """Heuristic: sum of Manhattan distances of tiles from their goal positions."""
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = goal_positions[val]
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist

def is_goal(state):
    return state == GOAL_STATE

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def generate_neighbors(state):
    neighbors = []
    x, y = find_zero(state)
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def a_star(start_state):
    open_set = []
    heapq.heappush(open_set, (h_manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while open_set:
        f, g, current_state, path = heapq.heappop(open_set)
        state_key = state_to_tuple(current_state)

        if state_key in visited:
            continue
        visited.add(state_key)

        if is_goal(current_state):
            return path + [current_state]

        for neighbor in generate_neighbors(current_state):
            neighbor_key = state_to_tuple(neighbor)
            if neighbor_key not in visited:
                heapq.heappush(open_set, (
                    g + 1 + h_manhattan_distance(neighbor),
                    g + 1,
                    neighbor,
                    path + [current_state]
                ))

    return None

def print_path(path):
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()

if __name__ == "__main__":
    start = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]

    solution = a_star(start)
    if solution:
        print_path(solution)
        print(f"Total steps: {len(solution) - 1}")
    else:
        print("No solution found.")
