class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)
        else:
            self.graph[from_vertex] = [to_vertex]

    def matrix_to_graph(self, n, matrix):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    my_graph.add_edge(str(i + 1), str(j + 1))

    def shortest_distance(self, start_vertex):
        distances = {}  # словник для зберігання відстаней
        visited = set()  # множина для відслідковування відвіданих вершин
        queue = []  # список для обробки вершин

        distances[start_vertex] = 0  # Відстань від стартової вершини до себе самої дорівнює 0
        visited.add(start_vertex)  # Додаємо стартову вершину до відвіданих

        queue.append(start_vertex)  # Додаємо стартову вершину до списку

        # Створимо список для зберігання відстаней для всіх вершин в порядку від 1 до n
        all_distances = [-1] * n
        all_distances[int(start_vertex) - 1] = 0

        while queue:
            current_vertex = queue.pop(0)

            for neighbor in self.graph.get(current_vertex, []):
                if neighbor not in visited:
                    distances[neighbor] = distances[current_vertex] + 1
                    visited.add(neighbor)
                    queue.append(neighbor)

                    # Оновимо відстані для всіх вершин в порядку від 1 до n
                    all_distances[int(neighbor) - 1] = distances[neighbor]
        return print(" ".join(map(str, all_distances)))

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {', '.join(neighbors)}")

# Створимо пустий граф
my_graph = Graph()

# Записую вхідні дані
n, x = map(int, input().split())

matrix = []
matrix = [[int(x) for x in input().split()] for i in range(n)]

# Додамо ребра графа
my_graph.matrix_to_graph(n, matrix)

# Виведемо граф
my_graph.print_graph()

# Виведемо знайдені відстані
my_graph.shortest_distance(str(x))