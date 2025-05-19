def dijkstra(graph, start, end=None):
    # Изначально все расстояния условно бесконечны (999)
    dist = {node: 999 for node in graph} 
    # Устанавливаем расстояние до стартовой вершины равной 0
    dist[start] = 0
    # Очередь, изначально содержит только передаваемую в функцию вершину
    queue = [start]
    # Словарь для хранения предков вершин (для дальнейшего восстановления пути)
    previous = {node: None for node in graph}

    # Условие выполняется пока очередь не пуста
    while queue:
        # Выбираем первую вершину из очереди, (удаляя ее из очереди)
        current_node = queue.pop(0)

        # Завершение цикла в случае достижения конечной вершины
        if end is not None and current_node == end:
            break

        # Проходим по всем смежным вершинам
        for neighbor in graph[current_node]:
            # Поиск короткого пути для смежной вершины
            # Если значение расстояние смежной вершины больше чем значение расстояние для текущей вершины +1 
            if dist[neighbor] > dist[current_node] + 1:
                dist[neighbor] = dist[current_node] + 1

                # Записываем предка для вершины
                previous[neighbor] = current_node
                # Добавляем смежную вершину в очередь, и повторяем цикл для нее
                queue.append(neighbor)

    # Если указана конечная вершина - возвращаем расстояние и путь
    if end is not None:
        # Восстанавливаем путь от end до start, в начале путь пуст
        path = []
        # Текущая вершина = конечной вершине
        current = end
        # Пока есть текущие веришны выполняем цикл
        while current is not None:
            # В путь добавляем текущую вершину
            path.append(current)
            # Из словаря предков достаем предка текущей вершины и делаем эту вершину текущей
            current = previous[current]

        # Разворачиваем путь (так он от последней найденной вершины ддо начальной)
        path.reverse()

        if path[0] == start:
            return dist[end], path    
        else:
            return None
    # Иначе возвращаем расстояния    
    else:
        return dist

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


# Начальная и конечная вершины
start_node = 'A'
end_node = 'M'

# Все расстояния
all_distances = dijkstra(graph, start_node)
print("Расстояния от начальной вершины:")
print(all_distances)

# Расстояние и путь до конкретной вершины (при наличии значения в переменной end) 
if end_node:
    distance, path = dijkstra(graph, start_node, end_node)
    print(f"Кратчайшее расстояние от {start_node} до {end_node} = {distance}")
    print(f"Оптимальный путь: {' -> '.join(path)}")
