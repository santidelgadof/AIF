from collections import deque
from problem import is_goal, MOVES
from node import Node
from state import State

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
        return start_node.path(), 0, 0

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
            
            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Generado objetivo -> {child.state} (g={child.g}, d={child.depth})\n")

                # Muestra todos los nodos ya visitados y los de la frontera restantes hasta el nodo meta
                goal_visited = False
                while goal_visited is False and frontier:
                    n = frontier.popleft()
                    explored.append(n.state)
                    if is_goal(n.state, goal):
                        goal_visited = True
                        break
                print(f"Nodos visitados:")
                for e in explored:
                    print(f"  {e}")

                return child.path(), len(explored), len(frontier) # TODO al hacer pop en frontier los borro
            
            frontier.append(child)
            frontier_set.add(state_right)
            generated.append((child.op, child.state))

        # 2. Mover
        dx, dy = MOVES[o]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            move_state = State(nx, ny, o)
            if move_state not in explored and move_state not in frontier_set:
                move_cost = matrix[nx][ny]
                child = Node(move_state, node, "move", node.g + move_cost, node.depth + 1)
                
                if is_goal(child.state, goal):
                    if verbose:
                        print(f"  Generado objetivo -> {child.state} (g={child.g}, d={child.depth})\n")
                    
                    # Muestra todos los nodos ya visitados y los de la frontera restantes hasta el nodo meta
                    goal_visited = False
                    while goal_visited is False and frontier:
                        n = frontier.popleft()
                        explored.append(n.state)
                        if is_goal(n.state, goal):
                            goal_visited = True
                            break
                    print(f"Nodos visitados:")
                    for e in explored:
                        print(f"  {e}")

                    return child.path(), len(explored), len(frontier) # TODO al hacer pop en frontier los borro
                
                frontier.append(child)
                frontier_set.add(move_state)
                generated.append((child.op, child.state))

        # 3. Girar izquierda
        o_left = (o - 1) % 8
        state_left = State(x, y, o_left)
        if state_left not in explored and state_left not in frontier_set:
            child = Node(state_left, node, "rotate_left", node.g + 1, node.depth + 1)
            
            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Generado objetivo -> {child.state} (g={child.g}, d={child.depth})\n")
                
                # Muestra todos los nodos ya visitados y los de la frontera restantes hasta el nodo meta
                goal_visited = False
                while goal_visited is False and frontier:
                    n = frontier.popleft()
                    explored.append(n.state)
                    if is_goal(n.state, goal):
                        goal_visited = True
                        break
                print(f"Nodos visitados:")
                for e in explored:
                    print(f"  {e}")
                
                return child.path(), len(explored), len(frontier) # TODO al hacer pop en frontier los borro
            
            frontier.append(child)
            frontier_set.add(state_left)
            generated.append((child.op, child.state))

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
    return None, len(explored), len(frontier)

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
        return start_node.path(), 0, 0

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

        # 1. Girar izquierda (se explorará el último)
        o_left = (o - 1) % 8
        state_left = State(x, y, o_left)
        if state_left not in explored and state_left not in frontier_set:
            child = Node(state_left, node, "rotate_left", node.g + 1, node.depth + 1)
            
            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Generado objetivo -> {child.state} (g={child.g}, d={child.depth})\n")
                
                # TODO
                # Muestra todos los nodos ya visitados y los de la frontera restantes hasta el nodo meta
                # goal_visited = False
                # while goal_visited is False and frontier:
                #     n = frontier.popleft()
                #     explored.append(n.state)
                #     if is_goal(n.state, goal):
                #         goal_visited = True
                #         break
                # print(f"Nodos visitados:")
                # for e in explored:
                #     print(f"  {e}")

                return child.path(), len(explored), len(frontier)

            frontier.append(child)
            frontier_set.add(state_left)
            generated.append((child.op, child.state))

        # 2. Mover
        dx, dy = MOVES[o]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            move_state = State(nx, ny, o)
            if move_state not in explored and move_state not in frontier_set:
                move_cost = matrix[nx][ny]
                child = Node(move_state, node, "move", node.g + move_cost, node.depth + 1)
                
                if is_goal(child.state, goal):
                    if verbose:
                        print(f"  Generado objetivo -> {child.state} (g={child.g}, d={child.depth})\n")
                    
                    # TODO
                    # Muestra todos los nodos ya visitados y los de la frontera restantes hasta el nodo meta
                    # goal_visited = False
                    # while goal_visited is False and frontier:
                    #     n = frontier.popleft()
                    #     explored.append(n.state)
                    #     if is_goal(n.state, goal):
                    #         goal_visited = True
                    #         break
                    # print(f"Nodos visitados:")
                    # for e in explored:
                    #     print(f"  {e}")

                    return child.path(), len(explored), len(frontier)
                
                frontier.append(child)
                frontier_set.add(move_state)
                generated.append((child.op, child.state))

        # 3. Girar derecha (se explorará primero)
        o_right = (o + 1) % 8
        state_right = State(x, y, o_right)
        if state_right not in explored and state_right not in frontier_set:
            child = Node(state_right, node, "rotate_right", node.g + 1, node.depth + 1)
            
            if is_goal(child.state, goal):
                if verbose:
                    print(f"  Generado objetivo -> {child.state} (g={child.g}, d={child.depth})\n")

                # TODO
                # Muestra todos los nodos ya visitados y los de la frontera restantes hasta el nodo meta
                # goal_visited = False
                # while goal_visited is False and frontier:
                #     n = frontier.popleft()
                #     explored.append(n.state)
                #     if is_goal(n.state, goal):
                #         goal_visited = True
                #         break
                # print(f"Nodos visitados:")
                # for e in explored:
                #     print(f"  {e}")

                return child.path(), len(explored), len(frontier)
            
            frontier.append(child)
            frontier_set.add(state_right)
            generated.append((child.op, child.state))

        # Para imprimir en el orden correcto (right, move, left) simplemente invertimos
        generated_rev = list(reversed(generated))

        # Imprimir sucesores generados y estado de la frontera
        if verbose:
            if generated_rev:
                gen_str = ", ".join([f"{op}:{st}" for op, st in generated_rev])
                print(f"  Generados -> {gen_str}")
            else:
                print("  (Sin sucesores nuevos)")
            frontier_states = [f"{n.state}" for n in frontier]
            print(f"  Frontera: {frontier_states}\n")

    if verbose:
        print("No se alcanzó la meta.")
    return None, len(explored), len(frontier)
