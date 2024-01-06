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

    def convert_to_tree(self, root_vertex):
        # Створюємо новий граф для дерева
        tree = Graph()
        # Створюємо список для черги BFS
        queue = []
        # Позначаємо початкову вершину як відвідану
        visited = set()
        visited.add(root_vertex)
        # Додаємо початкову вершину в чергу
        queue.append(root_vertex)

        while queue:
            current_vertex = queue.pop(0)
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    # Додаємо вершину і ребро до дерева
                    tree.add_vertex(neighbor)
                    tree.add_edge(current_vertex, neighbor)
                    # Позначаємо вершину як відвідану
                    visited.add(neighbor)
                    # Додаємо вершину до черги для подальшого обходу
                    queue.append(neighbor)

        return tree

    def print_edges(self):
        for vertex, neighbors in self.graph.items():
            for neighbor in neighbors:
                if vertex < neighbor:
                    print(f"{vertex} {neighbor}")

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {neighbors}")

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

tree = my_graph.convert_to_tree(root_vertex=1)
#tree.print_graph()
tree.print_edges()

# Виведемо граф
#my_graph.print_graph()
