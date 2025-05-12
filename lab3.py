import networkx as nx
import matplotlib.pyplot as plt

# Параметры графа полученные от преподователя
n = 15
p = 0.85

# Генерация граф Эрдёша-Реньи
G = nx.erdos_renyi_graph(n, p)

# Вычисление средней степени вершины
average = 0
for i in G.nodes():
    average = average + G.degree(i)
average = (float(average) / len(G.nodes()))

# Значение средней степени вершины по формуле (n-1)*p из лекции
t_average = (n - 1) * p

# Нахождение разницы значения степени вершины и значения средней степени вершины по формуле (n-1)*p
difference = abs(average - t_average)

# Вывод результатов
print(f"Средняя степень вершины в графе: {average:.2f}")
print(f"Теоретическое значение средней степени вершины (n-1)*p: {t_average:.2f}")
print(f"Разница между значениями: {difference:.2f}")