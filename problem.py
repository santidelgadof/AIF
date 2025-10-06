from state import State

# Orientaciones (dx, dy)
MOVES = [
    (-1, 0),   # 0: North
    (-1, 1),   # 1: NE
    (0, 1),    # 2: East
    (1, 1),    # 3: SE
    (1, 0),    # 4: South
    (1, -1),   # 5: SW
    (0, -1),   # 6: West
    (-1, -1),  # 7: NW
]

def load_map(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    rows, cols = map(int, lines[0].split())
    matrix = [list(map(int, lines[i].split())) for i in range(1, 1 + rows)]

    x0, y0, o0 = map(int, lines[1 + rows].split())
    xt, yt, ot = map(int, lines[2 + rows].split())

    start = State(x0, y0, o0)
    goal = State(xt, yt, ot)

    return rows, cols, matrix, start, goal

def successors(state: State, matrix):
    rows, cols = len(matrix), len(matrix[0])
    x, y, o = state.x, state.y, state.o
    succs = []

    # 1) rotate_right
    succs.append(("rotate_right", State(x, y, (o + 1) % 8), 1))

    # 2) move (si cabe)
    dx, dy = MOVES[o]
    nx, ny = x + dx, y + dy
    if 0 <= nx < rows and 0 <= ny < cols:
        succs.append(("move", State(nx, ny, o), matrix[nx][ny]))

    # 3) rotate_left
    succs.append(("rotate_left", State(x, y, (o - 1) % 8), 1))

    return succs

def is_goal(state: State, goal: State):
    if goal.o == 8:
        return state.x == goal.x and state.y == goal.y
    return state == goal
