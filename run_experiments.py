"""
Script to generate random maps and run performance experiments
for the search algorithms comparison.

This script will:
1. Generate random maps of different sizes (3x3, 5x5, 7x7, 9x9)
2. Run all three algorithms (BFS, DFS, A*) on each map
3. Collect statistics (depth, cost, nodes explored, frontier size)
4. Average results over 5 trials per size
5. Output formatted tables for the LaTeX report
"""

import random
import sys
from problem import load_map, State
from search import bfs, dfs, astar


def generate_random_map(n, output_file, start_pos=(0, 0), goal_pos=None, 
                       min_hardness=1, max_hardness=5):
    """
    Generate a random map and save to file.
    
    Args:
        n: Map size (n x n)
        output_file: Path to save the map
        start_pos: Starting position (x, y)
        goal_pos: Goal position (x, y), defaults to (n-1, n-1)
        min_hardness: Minimum cell hardness
        max_hardness: Maximum cell hardness
    """
    if goal_pos is None:
        goal_pos = (n-1, n-1)
    
    with open(output_file, 'w') as f:
        # Write dimensions
        f.write(f"{n} {n}\n")
        
        # Write hardness matrix
        for i in range(n):
            row = [str(random.randint(min_hardness, max_hardness)) 
                   for _ in range(n)]
            f.write(" ".join(row) + "\n")
        
        # Write start position (orientation 0 = North)
        f.write(f"{start_pos[0]} {start_pos[1]} 0\n")
        
        # Write goal position (orientation 8 = any)
        f.write(f"{goal_pos[0]} {goal_pos[1]} 8\n")


def run_algorithm(algo_name, start, goal, matrix):
    """
    Run a search algorithm and return statistics.
    
    Returns:
        dict with keys: depth, cost, explored, frontier, success
    """
    try:
        if algo_name == "bfs":
            path, explored, frontier = bfs(start, goal, matrix, verbose=False)
        elif algo_name == "dfs":
            path, explored, frontier = dfs(start, goal, matrix, verbose=False)
        elif algo_name == "astar":
            path, explored, frontier = astar(start, goal, matrix, verbose=False)
        else:
            return None
        
        if path:
            # Last node in path has final depth and cost
            final_state, final_cost, final_depth, final_op = path[-1]
            return {
                'depth': final_depth,
                'cost': final_cost,
                'explored': len(explored),
                'frontier': len(frontier),
                'success': True
            }
        else:
            return {
                'depth': 0,
                'cost': 0,
                'explored': len(explored),
                'frontier': len(frontier),
                'success': False
            }
    except Exception as e:
        print(f"Error running {algo_name}: {e}")
        return None


def run_experiments(map_sizes=[3, 5, 7, 9], num_trials=5):
    """
    Run experiments for all map sizes and algorithms.
    
    Args:
        map_sizes: List of map dimensions to test
        num_trials: Number of random maps per size
    
    Returns:
        dict: Results organized by size and algorithm
    """
    results = {}
    
    for size in map_sizes:
        print(f"\n{'='*60}")
        print(f"Running experiments for {size}x{size} maps...")
        print(f"{'='*60}")
        
        size_results = {
            'bfs': {'depth': [], 'cost': [], 'explored': [], 'frontier': []},
            'dfs': {'depth': [], 'cost': [], 'explored': [], 'frontier': []},
            'astar': {'depth': [], 'cost': [], 'explored': [], 'frontier': []}
        }
        
        for trial in range(num_trials):
            print(f"\nTrial {trial + 1}/{num_trials}:")
            
            # Generate random map
            map_file = f"temp_map_{size}x{size}_trial{trial}.txt"
            generate_random_map(size, map_file)
            
            # Load map
            rows, cols, matrix, start, goal = load_map(map_file)
            
            # Run each algorithm
            for algo_name in ['bfs', 'dfs', 'astar']:
                print(f"  Running {algo_name.upper()}...", end=' ')
                
                stats = run_algorithm(algo_name, start, goal, matrix)
                
                if stats and stats['success']:
                    size_results[algo_name]['depth'].append(stats['depth'])
                    size_results[algo_name]['cost'].append(stats['cost'])
                    size_results[algo_name]['explored'].append(stats['explored'])
                    size_results[algo_name]['frontier'].append(stats['frontier'])
                    print(f"✓ (d={stats['depth']}, g={stats['cost']}, "
                          f"E={stats['explored']}, F={stats['frontier']})")
                else:
                    print("✗ (failed)")
            
            # Clean up temporary file
            import os
            try:
                os.remove(map_file)
            except:
                pass
        
        # Calculate averages
        results[size] = {}
        for algo_name in ['bfs', 'dfs', 'astar']:
            results[size][algo_name] = {
                'depth': sum(size_results[algo_name]['depth']) / len(size_results[algo_name]['depth']) if size_results[algo_name]['depth'] else 0,
                'cost': sum(size_results[algo_name]['cost']) / len(size_results[algo_name]['cost']) if size_results[algo_name]['cost'] else 0,
                'explored': sum(size_results[algo_name]['explored']) / len(size_results[algo_name]['explored']) if size_results[algo_name]['explored'] else 0,
                'frontier': sum(size_results[algo_name]['frontier']) / len(size_results[algo_name]['frontier']) if size_results[algo_name]['frontier'] else 0
            }
    
    return results


def format_latex_table(size, results):
    """
    Format results as a LaTeX table.
    
    Args:
        size: Map size (e.g., 3 for 3x3)
        results: Results dict for this size
    
    Returns:
        str: LaTeX table code
    """
    latex = f"""
\\begin{{table}}[H]
\\centering
\\caption{{Performance comparison for ${size}\\times{size}$ maps}}
\\begin{{tabular}}{{lcccc}}
\\toprule
\\textbf{{Algorithm}} & \\textbf{{d}} & \\textbf{{g}} & \\textbf{{\\#E}} & \\textbf{{\\#F}} \\\\
\\midrule
"""
    
    for algo_name, display_name in [
        ('bfs', 'Breadth-First Search'),
        ('dfs', 'Depth-First Search'),
        ('astar', 'A* (Euclidean + Rotation)')
    ]:
        r = results[algo_name]
        latex += f"{display_name} & {r['depth']:.1f} & {r['cost']:.1f} & {r['explored']:.1f} & {r['frontier']:.1f} \\\\\n"
    
    latex += """\\bottomrule
\\end{tabular}
\\end{table}
"""
    return latex


def main():
    """Main execution function."""
    print("=" * 60)
    print("Search Algorithms Performance Experiment")
    print("=" * 60)
    
    # Run experiments
    print("\nStarting experiments...")
    print("This may take a few minutes depending on map sizes.\n")
    
    results = run_experiments(map_sizes=[3, 5, 7, 9], num_trials=5)
    
    # Print summary
    print("\n" + "=" * 60)
    print("EXPERIMENT RESULTS SUMMARY")
    print("=" * 60)
    
    for size in [3, 5, 7, 9]:
        print(f"\n{size}x{size} Maps (averaged over 5 trials):")
        print(f"{'Algorithm':<30} {'d':>6} {'g':>8} {'#E':>8} {'#F':>8}")
        print("-" * 60)
        
        for algo_name, display_name in [
            ('bfs', 'Breadth-First Search'),
            ('dfs', 'Depth-First Search'),
            ('astar', 'A*')
        ]:
            r = results[size][algo_name]
            print(f"{display_name:<30} {r['depth']:>6.1f} {r['cost']:>8.1f} "
                  f"{r['explored']:>8.1f} {r['frontier']:>8.1f}")
    
    # Generate LaTeX tables
    print("\n" + "=" * 60)
    print("LATEX TABLES FOR REPORT")
    print("=" * 60)
    print("\nCopy the following tables into your report.tex file:")
    print("(Replace the existing placeholder tables in Section 4.2)\n")
    
    for size in [3, 5, 7, 9]:
        print(format_latex_table(size, results[size]))
    
    # Save to file
    with open("experiment_results.txt", "w") as f:
        f.write("EXPERIMENT RESULTS\n")
        f.write("=" * 60 + "\n\n")
        
        for size in [3, 5, 7, 9]:
            f.write(f"\n{size}x{size} Maps:\n")
            f.write(f"{'Algorithm':<30} {'d':>6} {'g':>8} {'#E':>8} {'#F':>8}\n")
            f.write("-" * 60 + "\n")
            
            for algo_name, display_name in [
                ('bfs', 'Breadth-First Search'),
                ('dfs', 'Depth-First Search'),
                ('astar', 'A*')
            ]:
                r = results[size][algo_name]
                f.write(f"{display_name:<30} {r['depth']:>6.1f} {r['cost']:>8.1f} "
                       f"{r['explored']:>8.1f} {r['frontier']:>8.1f}\n")
        
        f.write("\n\n" + "=" * 60 + "\n")
        f.write("LATEX TABLES\n")
        f.write("=" * 60 + "\n\n")
        
        for size in [3, 5, 7, 9]:
            f.write(format_latex_table(size, results[size]))
    
    print("\nResults also saved to: experiment_results.txt")
    print("\nDone! You can now update your LaTeX report with these tables.")


if __name__ == "__main__":
    main()
