import math

n = int(input()) # Кількість тестів

array = []

for i in range(n):
    numbers = list(map(int, input().split()))[1:] # m (1 ≤ m ≤ 100)
    array.append(numbers)

def NSD(a, b):
    while b:
        a, b = b, a % b
    return a

def NSK(a, b):
    return abs(a * b) // NSD(a, b)

def NSK_result(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = NSK(result, numbers[i])
    return result

for i in array:
    fin_result = NSK_result(i)
    print(fin_result)