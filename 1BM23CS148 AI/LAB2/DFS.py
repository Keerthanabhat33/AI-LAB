
from collections import deque

# Possible moves: up, down, left, right
moves = {
    "up": -3,
    "down": 3,
    "left": -1,
    "right": 1
}

# Check if a move is valid
def is_valid(pos, move):
    if move == "left" and pos % 3 == 0:
        return False
    if move == "right" and pos % 3 == 2:
        return False
    if move == "up" and pos < 3:
        return False
    if move == "down" and pos > 5:
        return False
    return True

# Get all next states from current state
def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)

    for move, delta in moves.items():
        if is_valid(zero_pos, move):
            new_pos = zero_pos + delta
            new_state = list(state)
            # Swap blank with neighbor
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))
    return neighbors

# DFS implementation
def dfs(start, goal):
    stack = [(start, [start])] # (current_state, path)
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path # solution found

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None # No solution found


# Example usage
if __name__ == "__main__":
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

    solution = dfs(start, goal)

    if solution:
        print("Solution found in", len(solution) - 1, "moves:")
        for step in solution:
            print(step[0:3])
            print(step[3:6])
            print(step[6:9])
            print()
    else:
        print("No solution found.")

