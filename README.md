# AIF

Entrada: se carga un mapa desde un .txt con la matriz de durezas, el estado inicial y el estado meta.

Estado: definido como (x, y, orientación).

Acciones: rotate_left, rotate_right (coste = 1) y move (coste = dureza de la celda destino).

Sucesores: generados con la función successors, validando movimientos dentro del mapa.

# BFS / DFS: implementados en search.py.

BFS usa una cola (deque) y explora por niveles.

DFS usa una pila (stack) y explora en profundidad.

Salida: para cada nodo del camino se muestra (d, g, op, S)

d: profundidad en el árbol.

g: coste acumulado.

op: operador aplicado.

S: estado alcanzado.



# También se imprimen estadísticas:

Explorados: número total de nodos expandidos.

Frontera: nodos que quedaron en la frontera al terminar.

Con esto ya es posible ejecutar:

python main.py exampleMap.txt bfs
python main.py exampleMap.txt dfs