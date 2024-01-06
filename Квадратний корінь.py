C = float(input()) # Одне дійсне число С (1.0 ≤ C ≤ 10^10)

a = 0
b = C

epsilon = 1e-6

while (b - a) > epsilon:
    c = (a + b) / 2
    func = c ** 2 + c**(1/2) - C

    if func == 0:
        break
    elif func * (a ** 2 + a**(1/2) - C) < 0:
        b = c
    else:
        a = c

x = (a + b) / 2
print("{:.6f}".format(x))
