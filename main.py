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
        print("Camino encontrado:\n")
        for state, g, d, op in path:
            print(f"(d={d}, g={g}, op={op}, S={state})")
        print("\nExplorados:", explored) # TODO debe mostrar la lista creo
        print("Frontera:", frontier) # TODO debe mostrar la lista creo
    else:
        print("No se encontró solución")
