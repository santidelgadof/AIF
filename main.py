import sys
from problem import load_map
from search import bfs, dfs, astar, heuristic

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <map_file.txt> <algorithm> [--verbose|-v]")
        print("Available algorithms: bfs, dfs, astar")
        sys.exit(1)

    map_file = sys.argv[1]
    algo = sys.argv[2]
    verbose = any(arg in ("--verbose", "-v") for arg in sys.argv[3:])

    rows, cols, matrix, start, goal = load_map(map_file)

    if algo == "bfs":
        path, explored, frontier = bfs(start, goal, matrix, verbose=verbose)
    elif algo == "dfs":
        path, explored, frontier = dfs(start, goal, matrix, verbose=verbose)
    elif algo == "astar":
        path, explored, frontier = astar(start, goal, matrix, verbose=verbose)
    else:
        print("Algorithm not recognized (use bfs, dfs or astar)")
        sys.exit(1)

    if path:
        # Node 0
        state0, g0, d0, op0 = path[0]
        if verbose:
            print("\n\n-------------------------------------------------\n\n")
        print(f"\nNode 0 (starting node)")
        if algo == "astar":
            h0 = heuristic(state0, goal)
            print(f"  ({d0}, {g0}, {op0}, {h0:.2f}, {state0})")
        else:
            print(f"  ({d0}, {g0}, {op0}, {state0})")

        # Remaining nodes
        for i in range(1, len(path)):
            state, g, d, op = path[i]
            print(f"\nOperator {i}")
            print(f"  {op}")
            print(f"Node {i}")
            if algo == "astar":
                hi = heuristic(state, goal)
                print(f"  ({d}, {g}, {op}, {hi:.2f}, {state})")
            else:
                print(f"  ({d}, {g}, {op}, {state})")
        
        # Final statistics
        print(f"\nTotal number of items in explored list: {len(explored)}")
        print(f"Total number of items in frontier: {len(frontier)}")
    else:
        print("No solution found")
