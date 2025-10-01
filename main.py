import sys
from problem import load_map
from search import bfs, dfs

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python main.py <map_file.txt> <algoritmo> [--verbose|-v]")
        print("Algoritmos disponibles: bfs, dfs")
        sys.exit(1)

    map_file = sys.argv[1]
    algo = sys.argv[2]
    verbose = any(arg in ("--verbose", "-v") for arg in sys.argv[3:])

    rows, cols, matrix, start, goal = load_map(map_file)

    if algo == "bfs":
        path, explored, frontier = bfs(start, goal, matrix, verbose=verbose)
    elif algo == "dfs":
        path, explored, frontier = dfs(start, goal, matrix, verbose=verbose)
    else:
        print("Algoritmo no reconocido (usa bfs o dfs)")
        sys.exit(1)

    if path:
        # Formato según la especificación de la práctica (Sección 4.2)
        # Node 0 (starting node)
        # Operator 1
        # Node 1
        # ...
        
        # Primer nodo (inicial)
        state0, g0, d0, op0 = path[0]
        if verbose:
            print("\n\n-------------------------------------------------\n\n")
        print(f"\nNode 0 (starting node)")
        print(f"  ({d0}, {g0}, {op0}, {state0})")
        
        # Resto de nodos con sus operadores
        for i in range(1, len(path)):
            state, g, d, op = path[i]
            print(f"\nOperator {i}")
            print(f"  {op}")
            print(f"Node {i}")
            print(f"  ({d}, {g}, {op}, {state})")
        
        # Estadísticas finales
        print(f"\nTotal number of items in explored list: {len(explored)}")
        print(f"Total number of items in frontier: {len(frontier)}")
    else:
        print("No se encontró solución")
