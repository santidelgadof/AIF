from collections import deque
from problem import is_goal, MOVES
from node import Node
from state import State
import math, itertools, heapq

# -----------------------------
# Breadth-First Search (BFS)
# -----------------------------
def bfs(start, goal, matrix, verbose: bool = False):
    """
    Búsqueda en anchura (BFS) adaptada al problema:
    - Orden de generación de sucesores: girar_derecha, mover, girar_izquierda.
    - Se evita introducir en la frontera estados ya explorados o ya presentes en la propia frontera.
    - Se imprime paso a paso la expansión si verbose=True.
    """

    start_node = Node(start, None, "START", 0, 0)

    # Comprobación de si el estado inicial ya es meta
    if is_goal(start, goal):
        if verbose:
            print(f"GOAL (inicio) alcanzado: {start} | coste=0 | profundidad=0")
        
        return start_node.path(), [start], []

    frontier = deque([start_node]) # cola para nodos por explorar
    frontier_set = {start} # estados en la frontera para evitar duplicados
    explored: list[State] = [] # estados ya explorados
    step = 0

    while frontier:
        node = frontier.popleft()
        frontier_set.discard(node.state)

        # Verificar si ya ha sido explorado
        if node.state in explored:
            continue

        # Añadir a explorados
        explored.append(node.state)

        # Imprimir expansión si verbose=True
        if verbose:
            print(f"[Paso {step}] Expandir: {node.state} (g={node.g}, d={node.depth})")
            step += 1

        # Generación de sucesores (gir_der -> mover -> gir_izq)
        x, y, o = node.state.x, node.state.y, node.state.o
        rows, cols = len(matrix), len(matrix[0])

        generated = []  # lista para impresión

        # 1. Girar derecha
        o_right = (o + 1) % 8
        state_right = State(x, y, o_right)
        if state_right not in explored and state_right not in frontier_set:
            child = Node(state_right, node, "rotate_right", node.g + 1, node.depth + 1)
            
            frontier.append(child)
            frontier_set.add(state_right)
            generated.append((child.op, child.state))

            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Meta descubierta -> {child.state} (g={child.g}, d={child.depth})\n")

                return child.path(), explored, [n.state for n in frontier]

        # 2. Mover
        dx, dy = MOVES[o]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            move_state = State(nx, ny, o)
            if move_state not in explored and move_state not in frontier_set:
                move_cost = matrix[nx][ny]
                child = Node(move_state, node, "move", node.g + move_cost, node.depth + 1)
                                
                frontier.append(child)
                frontier_set.add(move_state)
                generated.append((child.op, child.state))

                if is_goal(child.state, goal):
                    if verbose:
                        print(f"  Meta descubierta -> {child.state} (g={child.g}, d={child.depth})\n")

                    return child.path(), explored, [n.state for n in frontier]


        # 3. Girar izquierda
        o_left = (o - 1) % 8
        state_left = State(x, y, o_left)
        if state_left not in explored and state_left not in frontier_set:
            child = Node(state_left, node, "rotate_left", node.g + 1, node.depth + 1)
                        
            frontier.append(child)
            frontier_set.add(state_left)
            generated.append((child.op, child.state))
            
            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Meta descubierta -> {child.state} (g={child.g}, d={child.depth})\n")
                
                return child.path(), explored, [n.state for n in frontier]


        # Imprimir sucesores generados y estado de la frontera
        if verbose:
            if generated:
                gen_str = ", ".join([f"{op}:{st}" for op, st in generated])
                print(f"  Generados -> {gen_str}")
            else:
                print("  (Sin sucesores nuevos)")
            frontier_states = [f"{n.state}" for n in frontier]
            print(f"  Frontera: {frontier_states}\n")

    # Sin solución
    if verbose:
        print("No se alcanzó la meta.")
 
    return None, explored, [n.state for n in frontier]

# -----------------------------
# Depth-First Search (DFS)
# -----------------------------
def dfs(start, goal, matrix, verbose: bool = False):
    """
    Depth-First Search (DFS) adaptada al problema:
    - Orden de generación de sucesores: girar_derecha, mover, girar_izquierda.
    - Se evita introducir en la frontera estados ya explorados o ya presentes en la propia frontera.
    - Se imprime paso a paso la expansión si verbose=True.
    """

    start_node = Node(start, None, "START", 0, 0)

    # Comprobación de si el estado inicial ya es meta
    if is_goal(start, goal):
        if verbose:
            print(f"GOAL (inicio) alcanzado: {start} | coste=0 | profundidad=0\n")

        return start_node.path(), [start], []

    frontier: list[Node] = [start_node] # pila para nodos por explorar
    frontier_set = {start} # estados en la frontera para evitar duplicados
    explored = set() # estados ya explorados
    step = 0

    while frontier:
        node = frontier.pop()
        frontier_set.discard(node.state)

        # Verificar si ya ha sido explorado
        if node.state in explored:
            continue

        # Añadir a explorados
        explored.add(node.state)

        # Imprimir expansión si verbose=True
        if verbose:
            print(f"[Paso {step}] Expandir: {node.state} (g={node.g}, d={node.depth})\n")
            step += 1

        # Generación de sucesores (gir_der -> mover -> gir_izq)
        x, y, o = node.state.x, node.state.y, node.state.o
        rows, cols = len(matrix), len(matrix[0])

        generated = []  # lista para impresión

        # Queremos que el orden de expansión sea: rotate_right -> move -> rotate_left, por lo 
        # que apilamos en orden inverso de exploración: rotate_left -> move -> rotate_right

        # 1. Girar izquierda (se apila primero, se explorará último)
        o_left = (o - 1) % 8
        state_left = State(x, y, o_left)
        added_left = False
        if state_left not in explored and state_left not in frontier_set:
            child = Node(state_left, node, "rotate_left", node.g + 1, node.depth + 1)
            
            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Meta descubierta -> {child.state} (g={child.g}, d={child.depth})\n")

                return child.path(), list(explored), [n.state for n in frontier]

            frontier.append(child)
            frontier_set.add(state_left)
            added_left = True

        # 2. Mover
        dx, dy = MOVES[o]
        nx, ny = x + dx, y + dy
        move_state = None
        added_move = False
        if 0 <= nx < rows and 0 <= ny < cols:
            move_state = State(nx, ny, o)
            if move_state not in explored and move_state not in frontier_set:
                move_cost = matrix[nx][ny]
                child = Node(move_state, node, "move", node.g + move_cost, node.depth + 1)
                
                if is_goal(child.state, goal):
                    if verbose:
                        print(f"  Meta descubierta -> {child.state} (g={child.g}, d={child.depth})\n")

                    return child.path(), list(explored), [n.state for n in frontier]
                
                frontier.append(child)
                frontier_set.add(move_state)
                added_move = True

        # 3. Girar derecha (se apila último, se explorará primero)
        o_right = (o + 1) % 8
        state_right = State(x, y, o_right)
        added_right = False
        if state_right not in explored and state_right not in frontier_set:
            child = Node(state_right, node, "rotate_right", node.g + 1, node.depth + 1)
            
            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Meta descubierta -> {child.state} (g={child.g}, d={child.depth})\n")

                return child.path(), list(explored), [n.state for n in frontier]
            
            frontier.append(child)
            frontier_set.add(state_right)
            added_right = True

        # Construir 'generated' en el orden de exploración (right, move, left)
        if added_right:
            generated.append(("rotate_right", state_right))
        if added_move:
            generated.append(("move", move_state))
        if added_left:
            generated.append(("rotate_left", state_left))

        # Imprimir sucesores generados y estado de la frontera
        if verbose:
            if generated:
                gen_str = ", ".join([f"{op}:{st}" for op, st in generated])
                print(f"  Generados -> {gen_str}")
            else:
                print("  (Sin sucesores nuevos)")
            frontier_states = [f"{n.state}" for n in reversed(frontier)]
            print(f"  Frontera: {frontier_states}\n")


    if verbose:
        print("No se alcanzó la meta.")
    return None, list(explored), [n.state for n in frontier]



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



def astar(start, goal, matrix, verbose=False):
    """
    A* que:
     - Solo inserta en la frontera si encuentra un mejor g para ese estado (decrease-key lógico).
     - Ignora entradas obsoletas del heap.
     - No reabre estados ya explorados (explored contains finalized g).
     - Imprime la frontera ordenada por f mostrando (estado, g, f).
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

        # Si la entrada del heap está obsoleta (no coincide con el mejor g que guardamos), la descartamos.
        best_g_for_state = frontier_best.get(node.state)
        if best_g_for_state is None or node.g != best_g_for_state:
            # entrada stale u ya retirada de frontier_best (por haber sido expandida)
            continue

        # Marcamos que ya no está en la frontera (porque vamos a expandirlo)
        del frontier_best[node.state]

        # Si ya fue explorado (finalizado) saltamos (con heurística consistente no debería ocurrir)
        if node.state in explored:
            continue

        # Finalizamos/expandimos este estado
        explored[node.state] = node.g

        # Comprobar objetivo
        if is_goal(node.state, goal):
            if verbose:
                print(f"GOAL alcanzado: {node.state} con coste={node.g}")
            # devolvemos frontier actual como lista limpia de estados (los que aún consideramos con mejor g)
            return node.path(), list(explored.keys()), list(frontier_best.keys())

        # Imprimir info del nodo que expandimos
        if verbose:
            hval = heuristic(node.state, goal)
            print(f"[Paso {step}] Expandir {node.state} | g={node.g}, h={hval:.2f}, f={node.g + hval:.2f}")
            step += 1

        generated = []

        # EXPANSIÓN: (1) girar derecha, (2) mover, (3) girar izquierda
        x, y, o = node.state.x, node.state.y, node.state.o
        rows, cols = len(matrix), len(matrix[0])

        # 1) Girar derecha
        o_right = (o + 1) % 8
        state_right = State(x, y, o_right)
        if state_right not in explored:
            g_new = node.g + 1
            # solo insertar si encontramos mejor g que el existente en la frontera
            if g_new < frontier_best.get(state_right, float('inf')):
                child = Node(state_right, node, "rotate_right", g_new, node.depth + 1)
                heapq.heappush(frontier, (g_new + heuristic(state_right, goal), next(counter), child))
                frontier_best[state_right] = g_new
                generated.append((child.op, child.state))

        # 2) Mover
        dx, dy = MOVES[o]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            move_state = State(nx, ny, o)
            if move_state not in explored:
                move_cost = matrix[nx][ny]
                g_new = node.g + move_cost
                if g_new < frontier_best.get(move_state, float('inf')):
                    child = Node(move_state, node, "move", g_new, node.depth + 1)
                    heapq.heappush(frontier, (g_new + heuristic(move_state, goal), next(counter), child))
                    frontier_best[move_state] = g_new
                    generated.append((child.op, child.state))

        # 3) Girar izquierda
        o_left = (o - 1) % 8
        state_left = State(x, y, o_left)
        if state_left not in explored:
            g_new = node.g + 1
            if g_new < frontier_best.get(state_left, float('inf')):
                child = Node(state_left, node, "rotate_left", g_new, node.depth + 1)
                heapq.heappush(frontier, (g_new + heuristic(state_left, goal), next(counter), child))
                frontier_best[state_left] = g_new
                generated.append((child.op, child.state))

        # IMPRESIÓN: sucesores generados
        if verbose:
            if generated:
                gen_str = ", ".join([f"{op}:{st}" for op, st in generated])
                print(f"  Generados -> {gen_str}")
            else:
                print("  (Sin sucesores nuevos)")

            # Para mostrar la frontera de forma ordenada por f, construimos un snapshot desde frontier_best:
            snapshot = []
            for st, gval in frontier_best.items():
                fval = gval + heuristic(st, goal)
                snapshot.append((fval, st, gval))
            snapshot.sort(key=lambda x: x[0])   # orden por f ascendente

            fr_str = [f"{st} g={gval} f={fval:.2f}" for (fval, st, gval) in snapshot]
            print(f"  Frontera (ordenada por f): {fr_str}\n")

    # Sin solución
    if verbose:
        print("No se alcanzó la meta.")
    return None, list(explored.keys()), list(frontier_best.keys())