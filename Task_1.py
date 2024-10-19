import networkx as nx
import matplotlib.pyplot as plt

# Створимо граф для моделювання простої транспортної мережі міста
# Приклад: транспортна мережа з 8 станцій (вершин) і 10 маршрутів (ребер)

# Створимо порожній граф
G = nx.Graph()

# Додаємо станції (вершини)
stations = ["Station A", "Station B", "Station C", "Station D", 
            "Station E", "Station F", "Station G", "Station H"]

# Додаємо маршрути (ребра між станціями)
routes = [("Station A", "Station B"), 
          ("Station A", "Station C"),
          ("Station B", "Station D"),
          ("Station C", "Station D"),
          ("Station C", "Station E"),
          ("Station D", "Station F"),
          ("Station E", "Station F"),
          ("Station E", "Station G"),
          ("Station F", "Station H"),
          ("Station G", "Station H")]

# Додаємо вершини та ребра до графа
G.add_nodes_from(stations)
G.add_edges_from(routes)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=12, font_color="black", edge_color="gray", width=2)

# Показуємо граф
plt.title("Transport Network Graph")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_distribution = dict(G.degree())

print("Кількість вершин:", num_nodes)
print("Кількість ребер:", num_edges)
print("Ступінь кожної вершини:", degree_distribution)
