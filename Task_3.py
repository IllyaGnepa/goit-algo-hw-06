import heapq

# Функція для реалізації алгоритму Дейкстри
def dijkstra(graph, start):
    # Словник для зберігання відстаней до всіх вершин
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0  # Відстань до стартової вершини = 0

    # Пріоритетна черга для вибору вершини з найменшою відстанню
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань до цієї вершини більше, ніж раніше знайдена, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Оновлюємо відстані до сусідніх вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо нова відстань менша, оновлюємо її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Додаємо ваги до ребер графа
weighted_graph = {
    "Station A": {"Station B": 2, "Station C": 4},
    "Station B": {"Station A": 2, "Station D": 1},
    "Station C": {"Station A": 4, "Station D": 2, "Station E": 3},
    "Station D": {"Station B": 1, "Station C": 2, "Station F": 5},
    "Station E": {"Station C": 3, "Station F": 2, "Station G": 2},
    "Station F": {"Station D": 5, "Station E": 2, "Station H": 1},
    "Station G": {"Station E": 2, "Station H": 3},
    "Station H": {"Station F": 1, "Station G": 3}
}

# Знаходимо найкороткі шляхи від Station A до всіх інших станцій
shortest_paths = dijkstra(weighted_graph, "Station A")
print("Найкоротші шляхи від Station A:", shortest_paths)
