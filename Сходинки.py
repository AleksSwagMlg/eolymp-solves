n = int(input()) #кількість сходинок  (0 ≤ n ≤ 1000)
b = list(map(int, input().split())) #числа
k = int(input()) #довжина кроку (1 ≤ k ≤ n)

a = [0] * (n + k + 1)

j = 0
for i in range(k, n + k):
    a[i] = b[j]
    j += 1

for i in range(k, k + n + 1):
    m = a[i - k]
    for j in range(i - k + 1, i):
        if m <= a[j]:
            m = a[j]
    a[i] += m

print(a[k + n])