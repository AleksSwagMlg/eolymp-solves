a, b = map(int, input().split()) # 1 ≤ a ≤ b ≤ 10

def Eratosfen_function(n):
    proste = [True] * (n + 1)
    proste[0] = proste[1] = False

    for p in range(2, int(n**0.5) + 1):
        if proste[p]:
            for i in range(p * p, n + 1, p):
                proste[i] = False

    prosti_chisla = []
    for i in range(2, n + 1):
        if proste[i]:
            prosti_chisla.append(i)

    return prosti_chisla

result = Eratosfen_function(b)

for number in result:
    if a <= number <= b:
        print(number, end=' ')