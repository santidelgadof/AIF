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
    Búsqueda en anchura (BFS):
    - Orden de sucesores: rotate_right -> move -> rotate_left (delegado a problem.successors).
    - Evita duplicados con frontier_set y explored.
    - Traza paso a paso si verbose=True.
    """
    start_node = Node(start, None, "START", 0, 0)

    # Caso trivial: inicio ya es meta
    if is_goal(start, goal):
        if verbose:
            print(f"GOAL (inicio) alcanzado: {start} | coste=0 | profundidad=0")
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
            print(f"[Paso {step}] Expandir: {node.state} (g={node.g}, d={node.depth})")
            step += 1

        generated = []
        # successors devuelve en orden: R, M, L
        for op, nxt, cost in successors(node.state, matrix):
            if nxt in explored or nxt in frontier_set:
                continue

            child = Node(nxt, node, op, node.g + cost, node.depth + 1)

            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Meta descubierta -> {child.state} (g={child.g}, d={child.depth})\n")
                return child.path(), list(explored), [n.state for n in frontier]

            frontier.append(child)
            frontier_set.add(nxt)
            generated.append((child.op, child.state))

        if verbose:
            if generated:
                gen_str = ", ".join([f"{op}:{st}" for op, st in generated])
                print(f"  Generados -> {gen_str}")
            else:
                print("  (Sin sucesores nuevos)")
            print(f"  Frontera: {[f'{n.state}' for n in frontier]}\n")

    if verbose:
        print("No se alcanzó la meta.")
    return None, list(explored), [n.state for n in frontier]


# ---------------------------------
# Depth-First Search (DFS)
# ---------------------------------
def dfs(start: State, goal: State, matrix, verbose: bool = False):
    """
    Depth-First Search (DFS):
    - Queremos explorar R -> M -> L, así que APILAMOS en orden inverso: L -> M -> R.
    - Evita duplicados con frontier_set y explored.
    - Traza si verbose=True.
    """
    start_node = Node(start, None, "START", 0, 0)

    if is_goal(start, goal):
        if verbose:
            print(f"GOAL (inicio) alcanzado: {start} | coste=0 | profundidad=0\n")
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
            print(f"[Paso {step}] Expandir: {node.state} (g={node.g}, d={node.depth})\n")
            step += 1

        # Sucesores R, M, L -> apilar al revés
        succs = list(successors(node.state, matrix))
        for op, nxt, cost in reversed(succs):
            if nxt in explored or nxt in frontier_set:
                continue

            child = Node(nxt, node, op, node.g + cost, node.depth + 1)
            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Meta descubierta -> {child.state} (g={child.g}, d={child.depth})\n")
                return child.path(), list(explored), [n.state for n in frontier]

            frontier.append(child)
            frontier_set.add(nxt)

        if verbose:
            generated = []
            for op, nxt, _ in succs:  # mostrar en orden de exploración (R, M, L)
                if nxt in frontier_set and nxt not in explored:
                    generated.append((op, nxt))
            if generated:
                print("  Generados -> " + ", ".join([f"{op}:{st}" for op, st in generated]))
            else:
                print("  (Sin sucesores nuevos)")
            # Snapshot de la pila (tope al final)
            print(f"  Frontera: {[f'{n.state}' for n in reversed(frontier)]}\n")

    if verbose:
        print("No se alcanzó la meta.")
    return None, list(explored), [n.state for n in frontier]


# ---------------------------------
# Heurística A*
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
     - Inserta en la frontera solo si mejora g para ese estado.
     - Ignora entradas obsoletas del heap.
     - No reabre estados ya cerrados (explored).
     - Usa successors() (orden R -> M -> L).
    """
    counter = itertools.count()
    start_node = Node(start, None, "START", 0, 0)

    # heap entries: (f, tie_breaker, node)
    frontier = []
    start_f = heuristic(start, goal) + start_node.g
    heapq.heappush(frontier, (start_f, next(counter), start_node))

    # frontier_best: estado -> mejor g actualmente en la frontera
    frontier_best = {start: start_node.g}

    # explored: estado -> mejor g ya expandido (cerrado)
    explored = {}

    step = 0

    while frontier:
        f_curr, _, node = heapq.heappop(frontier)

        # Entrada obsoleta (g ya no coincide con el mejor)
        best_g_for_state = frontier_best.get(node.state)
        if best_g_for_state is None or node.g != best_g_for_state:
            continue

        # Sacamos de la frontera y pasamos a cerrado
        del frontier_best[node.state]

        if node.state in explored:
            continue
        explored[node.state] = node.g

        # Objetivo
        if is_goal(node.state, goal):
            if verbose:
                print(f"GOAL alcanzado: {node.state} con coste={node.g}")
            return node.path(), list(explored.keys()), list(frontier_best.keys())

        if verbose:
            hval = heuristic(node.state, goal)
            print(f"[Paso {step}] Expandir {node.state} | g={node.g}, h={hval:.2f}, f={node.g + hval:.2f}")
            step += 1

        generated = []

        # EXPANSIÓN usando el orden R -> M -> L
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
                print(f"  Generados -> {gen_str}")
            else:
                print("  (Sin sucesores nuevos)")
            # Snapshot de frontera ordenada por f (a partir de frontier_best)
            snapshot = []
            for st, gval in frontier_best.items():
                fval = gval + heuristic(st, goal)
                snapshot.append((fval, st, gval))
            snapshot.sort(key=lambda x: x[0])
            fr_str = [f"{st} g={gval} f={fval:.2f}" for (fval, st, gval) in snapshot]
            print(f"  Frontera (ordenada por f): {fr_str}\n")

    if verbose:
        print("No se alcanzó la meta.")
    return None, list(explored.keys()), list(frontier_best.keys())
