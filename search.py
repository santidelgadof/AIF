from collections import deque
from problem import successors, is_goal

# -----------------------------
# Breadth-First Search (BFS)
# -----------------------------
def bfs(start, goal, matrix):
    frontier = deque([(start, [], 0, 0, "START")])  # (state, path, g, depth, op)
    explored = set()

    while frontier:
        state, path, g, d, op = frontier.popleft()

        if is_goal(state, goal):
            return path + [(state, g, d, op)], len(explored), len(frontier)

        if state in explored:
            continue
        explored.add(state)

        for action, new_state, cost in successors(state, matrix):
            if new_state not in explored:
                frontier.append((new_state, path + [(state, g, d, op)], g + cost, d + 1, action))

    return None, len(explored), len(frontier)


# -----------------------------
# Depth-First Search (DFS)
# -----------------------------
def dfs(start, goal, matrix):
    frontier = [(start, [], 0, 0, "START")]  # stack (state, path, g, depth, op)
    explored = set()

    while frontier:
        state, path, g, d, op = frontier.pop()

        if is_goal(state, goal):
            return path + [(state, g, d, op)], len(explored), len(frontier)

        if state in explored:
            continue
        explored.add(state)

        for action, new_state, cost in successors(state, matrix):
            if new_state not in explored:
                frontier.append((new_state, path + [(state, g, d, op)], g + cost, d + 1, action))

    return None, len(explored), len(frontier)
