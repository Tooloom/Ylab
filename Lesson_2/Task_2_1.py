# Перед тем, как заметил "Путём перебора длин всех возможных маршрутов найти самый короткий из них"
# в условии задачи - долго искал варианты оптимизированного поиска кратчайших путей в графах,
# такие как Алгоритм Дейкстры и т.д.
# В условиях задачи в конце показан пример вывода результатов на экран. Я сделал немного по-своему,
# ибо так более читаемо, как по мне.
# И там же, в этом примере - показан не самый оптимальный вариант, как я понял. Немного смутил этот
# момент. Надеюсь, задача коммивояжёра выполнена успешно.

from itertools import permutations
from math import inf

# ------------------- initialising -------------------
points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
postal_office = (0, 2)
arcs = {}

for i in points:
    points_2 = points[:]
    points_2.remove(i)
    for j in points_2:
        arcs[(i, j)] = ((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2) ** 0.5

# ------------------- looking for all the ways -------------------
path = [(postal_office, *i, postal_office) for i in permutations(points[1:], len(points) - 1)]

# ------------------- looking for the shortest path -------------------
shortest_path = inf  # infinite value for comparator
shortest_path_nodes = None

for i in path:
    temp = 0
    for j in range(len(i) - 1):
        temp += arcs[i[j], i[j + 1]]
    if temp < shortest_path:
        shortest_path = temp
        shortest_path_nodes = i

# ------------------- print results -------------------
print_temp = 0
for i in range(len(shortest_path_nodes) - 1):
    print_temp += arcs[shortest_path_nodes[i], shortest_path_nodes[i + 1]]
    print(f'{shortest_path_nodes[i]} -> {shortest_path_nodes[i + 1]}\t[{print_temp}]')

print(f'TOTAL:\t\t\t\t{shortest_path}')
