def find_maximum_shortest_distance(graph):
    n = len(graph)

    # Ініціалізація матриці відстаней та попередників
    dist = [row.copy() for row in graph]
    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1:
                dist[i][j] = float('inf')

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    max_distance = -1
    # Знаходження максимальної відстані
    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('inf') and dist[i][j] > max_distance:
                max_distance = dist[i][j]

    return max_distance


# Зчитування вхідних даних
n = int(input())
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Знаходження та виведення результату
result = find_maximum_shortest_distance(graph)
print(result)
