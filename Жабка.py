n = int(input()) #Кількість камінців 2 ≤ n ≤ 10^5
numbers = list(map(int, input().split())) #Числа 1 ≤ h[i] ≤ 10^4

help_array = [0] * n #Сюди буду записувати максимальні суми на i-му кроці

help_array[1] = abs(numbers[1] - numbers[0]) #База

for i in range(2, n):
    help_array[i] = min(help_array[i-1] + abs(numbers[i] - numbers[i-1]), help_array[i-2] + abs(numbers[i] - numbers[i-2]))

result = help_array[n-1]
print(result)