n = int(input()) #Kількість будинків 1 ≤ n ≤ 10^6
a = list(map(int, input().split())) #Кількість грошей в a[i] домі

A = [0] * n

if n == 1:
    print(a[0])
    exit()

A[0] = a[0]
A[1] = max(a[0], a[1])  #База

for i in range(2, n):
    A[i] = max(A[i-1], a[i] + A[i-2])

print(A[n-1])