from collections import deque

# Функція для пошуку шляху за допомогою DFS
def dfs_path(graph, start, goal):
    stack = [(start, [start])]  # Використовуємо стек для зберігання поточного шляху
    while stack:
        (vertex, path) = stack.pop()  # Виймаємо поточну вершину зі стеку
        for next_node in set(graph[vertex]) - set(path):  # Для всіх суміжних вершин, що не були в шляху
            if next_node == goal:
                return path + [next_node]  # Якщо знайшли ціль, повертаємо шлях
            else:
                stack.append((next_node, path + [next_node]))  # Додаємо вершину в стек і шлях

# Функція для пошуку шляху за допомогою BFS
def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])  # Використовуємо чергу для зберігання поточного шляху
    while queue:
        (vertex, path) = queue.popleft()  # Виймаємо поточну вершину з черги
        for next_node in set(graph[vertex]) - set(path):  # Для всіх суміжних вершин, що не були в шляху
            if next_node == goal:
                return path + [next_node]  # Якщо знайшли ціль, повертаємо шлях
            else:
                queue.append((next_node, path + [next_node]))  # Додаємо вершину в чергу і шлях

# Перетворимо наш граф на відповідну структуру для пошуку шляхів
graph = {
    "Station A": ["Station B", "Station C"],
    "Station B": ["Station A", "Station D"],
    "Station C": ["Station A", "Station D", "Station E"],
    "Station D": ["Station B", "Station C", "Station F"],
    "Station E": ["Station C", "Station F", "Station G"],
    "Station F": ["Station D", "Station E", "Station H"],
    "Station G": ["Station E", "Station H"],
    "Station H": ["Station F", "Station G"]
}

# Знайдемо шляхи між "Station A" і "Station H" для обох алгоритмів
dfs_result = dfs_path(graph, "Station A", "Station H")
bfs_result = bfs_path(graph, "Station A", "Station H")

print("DFS шлях:", dfs_result)
print("BFS шлях:", bfs_result)
