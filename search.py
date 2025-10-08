from collections import deque
from problem import is_goal, successors
from node import Node
from state import State
import math, itertools, heapq

# ---------------------------------
# Breadth-First Search (BFS)
# ---------------------------------
def bfs(start: State, goal: State, matrix, verbose: bool = False):
    """
    Breadth-First Search (BFS):
    - Successor order: rotate_right -> move -> rotate_left (delegated to problem.successors).
    - Avoids duplicates with frontier_set and explored.
    - Step-by-step trace if verbose=True.
    """
    start_node = Node(start, None, "START", 0, 0)

    # Start is already goal
    if is_goal(start, goal):
        if verbose:
            print(f"GOAL (start) reached: {start} | cost=0 | depth=0")
        return start_node.path(), [start], []

    frontier = deque([start_node])
    frontier_set = {start}
    explored: set[State] = set()
    step = 0

    while frontier:
        node = frontier.popleft()
        frontier_set.discard(node.state)

        if node.state in explored:
            continue
        explored.add(node.state)

        if verbose:
            print(f"[Step {step}] Expand: {node.state} (g={node.g}, d={node.depth})")
            step += 1

        generated = []
        # successors returns in order: R, M, L
        for op, nxt, cost in successors(node.state, matrix):
            if nxt in explored or nxt in frontier_set:
                continue

            child = Node(nxt, node, op, node.g + cost, node.depth + 1)
            frontier.append(child)
            frontier_set.add(nxt)
            generated.append((child.op, child.state))

            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Goal found -> {child.state} (g={child.g}, d={child.depth})\n")
                return child.path(), list(explored), [n.state for n in frontier]

        if verbose:
            if generated:
                gen_str = ", ".join([f"{op}:{st}" for op, st in generated])
                print(f"  Generated -> {gen_str}")
            else:
                print("  (No new successors)")
            print(f"  Frontier: {[f'{n.state}' for n in frontier]}\n")

    if verbose:
        print("Goal not reached.")
    return None, list(explored), [n.state for n in frontier]


# ---------------------------------
# Depth-First Search (DFS)
# ---------------------------------
def dfs(start: State, goal: State, matrix, verbose: bool = False):
    """
    Depth-First Search (DFS):
    - We want to explore R -> M -> L, so we STACK in reverse order: L -> M -> R.
    - Avoids duplicates with frontier_set and explored.
    - Trace if verbose=True.
    """
    start_node = Node(start, None, "START", 0, 0)

    if is_goal(start, goal):
        if verbose:
            print(f"GOAL (start) reached: {start} | cost=0 | depth=0\n")
        return start_node.path(), [start], []

    frontier: list[Node] = [start_node]
    frontier_set = {start}
    explored: set[State] = set()
    step = 0

    while frontier:
        node = frontier.pop()
        frontier_set.discard(node.state)

        if node.state in explored:
            continue
        explored.add(node.state)

        if verbose:
            print(f"[Step {step}] Expand: {node.state} (g={node.g}, d={node.depth})\n")
            step += 1

        # Successors R, M, L -> stack in reverse order
        succs = list(successors(node.state, matrix))
        for op, nxt, cost in reversed(succs):
            # If already explored, skip it
            if nxt in explored:
                continue

            # If already in frontier, remove it to reinsert
            if nxt in frontier_set:
                frontier = [n for n in frontier if n.state != nxt]
                frontier_set.remove(nxt)

            child = Node(nxt, node, op, node.g + cost, node.depth + 1)
            frontier.append(child)
            frontier_set.add(nxt)

            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Goal found -> {child.state} (g={child.g}, d={child.depth})\n")
                return child.path(), list(explored), [n.state for n in frontier]

        if verbose:
            generated = []
            for op, nxt, _ in succs:  # show in exploration order (R, M, L)
                if nxt in frontier_set and nxt not in explored:
                    generated.append((op, nxt))
            if generated:
                print("  Generated -> " + ", ".join([f"{op}:{st}" for op, st in generated]))
            else:
                print("  (No new successors)")
            # Stack snapshot (top at the end)
            print(f"  Frontier: {[f'{n.state}' for n in reversed(frontier)]}\n")

    if verbose:
        print("Goal not reached.")
    return None, list(explored), [n.state for n in frontier]


# ---------------------------------
# A* Heuristic
# ---------------------------------
def heuristic(state: State, goal: State):
    dx = goal.x - state.x
    dy = goal.y - state.y
    euclid = math.sqrt(dx*dx + dy*dy)

    if goal.o == 8:
        turn_cost = 0
    else:
        do = abs(goal.o - state.o) % 8
        turn_cost = min(do, 8 - do)

    return euclid + turn_cost


# ---------------------------------
# A* Search
# ---------------------------------
def astar(start: State, goal: State, matrix, verbose: bool = False):
    """
    A*:
     - Inserts into frontier only if it improves g for that state.
     - Ignores obsolete heap entries.
     - Does not reopen closed states (explored).
     - Uses successors() (order R -> M -> L).
    """
    counter = itertools.count()
    start_node = Node(start, None, "START", 0, 0)

    # heap entries: (f, tie_breaker, node)
    frontier = []
    start_f = heuristic(start, goal) + start_node.g
    heapq.heappush(frontier, (start_f, next(counter), start_node))

    # frontier_best: state -> best g currently in frontier
    frontier_best = {start: start_node.g}

    # explored: state -> best g already expanded (closed)
    explored = {}

    step = 0

    while frontier:
        f_curr, _, node = heapq.heappop(frontier)

        # Obsolete entry (g no longer matches best)
        best_g_for_state = frontier_best.get(node.state)
        if best_g_for_state is None or node.g != best_g_for_state:
            continue

        # Remove from frontier and move to closed
        del frontier_best[node.state]

        if node.state in explored:
            continue
        explored[node.state] = node.g

        # Goal test
        if is_goal(node.state, goal):
            if verbose:
                print(f"GOAL reached: {node.state} with cost={node.g}")
            return node.path(), list(explored.keys()), list(frontier_best.keys())

        if verbose:
            hval = heuristic(node.state, goal)
            print(f"[Step {step}] Expand {node.state} | g={node.g}, h={hval:.2f}, f={node.g + hval:.2f}")
            step += 1

        generated = []

        # EXPANSION using R -> M -> L order
        for op, nxt, cost in successors(node.state, matrix):
            if nxt in explored:
                continue

            g_new = node.g + cost
            if g_new < frontier_best.get(nxt, float('inf')):
                child = Node(nxt, node, op, g_new, node.depth + 1)
                f_new = g_new + heuristic(nxt, goal)
                heapq.heappush(frontier, (f_new, next(counter), child))
                frontier_best[nxt] = g_new
                generated.append((child.op, child.state))

        if verbose:
            if generated:
                gen_str = ", ".join([f"{op}:{st}" for op, st in generated])
                print(f"  Generated -> {gen_str}")
            else:
                print("  (No new successors)")
            # Frontier snapshot ordered by f (from frontier_best)
            snapshot = []
            for st, gval in frontier_best.items():
                fval = gval + heuristic(st, goal)
                snapshot.append((fval, st, gval))
            snapshot.sort(key=lambda x: x[0])
            fr_str = [f"{st} g={gval} f={fval:.2f}" for (fval, st, gval) in snapshot]
            print(f"  Frontier (ordered by f): {fr_str}\n")

    if verbose:
        print("Goal not reached.")
    return None, list(explored.keys()), list(frontier_best.keys())
