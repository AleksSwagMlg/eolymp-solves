n, k = map(int, input().split())
motuzky = [int(input()) for motuzka in range(n)]

low = 1
high = max(motuzky)
result = 0

def can_cut_motuzky(motuzky, k, length):
    count = 0
    for motuzka in motuzky:
        count += motuzka // length
    # Повертаємо значення, яке відповідає за те, чи вистачить нам мотузок
    return count >= k

while low <= high:
    mid = (low + high) // 2
    if can_cut_motuzky(motuzky, k, mid):
        # Якщо мотузок більше потрібного то збільшуємо мінімальний поріг, отже і середній розмір мотузки
        result = mid
        low = mid + 1
    else:
        # Якщо мотузок менше потрібного то зменшуємо максимальний поріг, отже і середній розмір мотузки
        high = mid - 1

print(result)