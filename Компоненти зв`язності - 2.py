class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)
        else:
            self.graph[vertex2] = [vertex1]

    def print_connected_components(self):
        visited = set()
        components = []

        for vertex in self.graph:
            if vertex not in visited:
                component = []
                self._dfs(vertex, visited, component)
                components.append(component)

        # Вивід остаточного результату
        print(len(components))
        for component in components:
            print(len((component)))
            print(' '.join(map(str, component)))

    def _dfs(self, vertex, visited, component):
        visited.add(vertex)
        component.append(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, component)

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")

# Створимо пустий граф
my_graph = Graph()

# Записую вхідні дані
N, M = map(int, input().split())

# Додаємо точки
for i in range(1, N+1):
    my_graph.add_vertex(i)

# Додамо ребра
for i in range(M):
    k, l = map(int, input().split())
    my_graph.add_edge(k, l)

# Виведемо граф
#my_graph.print_graph()
my_graph.print_connected_components()