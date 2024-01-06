import math

n = int(input()) # Кількість чисел  (1 < n < 21)

numbers = list(map(int, input().split())) # m (1 ≤ m ≤ 100)

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

print(NSK_result(numbers))