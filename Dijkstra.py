def dijkstra(graph, start):
    # Изначально все расстояния бесконечны (float('infinity'))
    dist = {node: float('infinity') for node in graph} 
    # Устанавливаем расстояние до стартовой вершины равной 0
    dist[start] = 0
    previous = {node: None for node in graph}
    # Множество непосещённых вершин. Содержит все вершины графа, по мере работы из него удаляются посещённые вершины.
    unvisited = set(graph.keys())

    while unvisited:
        # На каждом шаге обрабатываем вершину с наименьшим известным расстоянием от стартовой вершины
        # Выбираем вершину с минимальным расстоянием (на первой итерации это start_node)
        current_node = min(unvisited, key=lambda v: dist[v])

        # Если минимальное расстояние - бесконечность, остальные вершины недостижимы
        if dist[current_node] == float('infinity'):
            break

        # Обновляем расстояния до соседей (вес ребра = 1)
        for neighbor in graph[current_node]:
            distance = dist[current_node] + 1  # Все рёбра имеют вес 1
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                # Сохраняем информацию о родительской вершине для построения обратного пути
                previous[neighbor] = current_node
                
        # Отмечаем вершину как посещённую (убираем из множества непосещённых вершин)
        unvisited.remove(current_node)
    return dist, previous

# Функция восстановления пути
def get_shortest_path(previous, start_node, target):
    path = []
    current = target
    
    while current != start_node:
        path.append(current)
        current = previous[current]
        if current is None:  # Путь не существует
            return None
            
    path.append(start_node)
    path.reverse()
    return path


# Граф (список смежности)
graph = {
'A': ['B', 'D', 'I', 'H' ], 
'B': ['C', 'F', 'I', 'E', 'J'], 
'C': ['G', 'F', 'L', 'B', 'A', 'I'], 
'D': ['F'], 
'E': ['D', 'J', 'B', 'K'], 
'F': ['D', 'M', 'G', 'A', 'C', 'E'], 
'G': ['L', 'B', 'F', 'C', 'E'], 
'H': ['F'], 
'I': ['D'], 
'J': ['M', 'F'], 
'K': ['L', 'G', 'H', 'B'], 
'L': ['K', 'H'], 
'M': ['J', 'I', 'L']
}

# Начальниая вершина
start_node = 'A'
dist, previous = dijkstra(graph, start_node)

print("Кратчайшие расстояния:")
for node in dist:
    print(f"{start_node} -> {node}: {dist[node]}")
print('_______________________')
print("Кратчайшие пути:")

for node in graph:
    path = get_shortest_path(previous, start_node, node)
    if path:
        print(f"от {start_node} до {node}: {' -> '.join(path)}")
    else: 
        print('Нет пути')
