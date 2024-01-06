import math

n = int(input()) # Кількість елементів у масиві n (n ≤ 100)
numbers = list(map(float, input().split())) # m (-100 ≤ m ≤ 100)

min = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] < min:
        min = numbers[i]

result = min * 2
print(f'{result:.2f}')