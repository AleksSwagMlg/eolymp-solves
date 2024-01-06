n, k = list(map(int, input().split()))

A = [0] * (n + 1)

A[1] = 1 #База

for i in range(2, n+1):
    for j in range(1, k+1):
        A[i] += A[i-j]

print(A[n])