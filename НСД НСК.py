import math

T = int(input()) # T ≤ 100

array = []

for i in range(T):
    G, L = map(int, input().split()) # G і L < 231
    array.append((G, L))

def find_a_b(T, test_cases):
    result = []
    for i in range(T):
        G, L = test_cases[i]
        if L % G == 0:
            a = G
            b = L
            result.append((a, b))
        else:
            result.append((-1,))
    return result

results = find_a_b(T, array)

for result in results:
    if result[0] == -1:
        print(-1)
    else:
        print(result[0], result[1])
