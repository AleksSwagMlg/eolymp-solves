n = input() #кількість видів метеликів (0 ≤ n ≤ 10^5)
numbers = input().split() #номери видів метеликів у колекції
m = input() #кількість запитів  (1 ≤ m ≤ 10^5)
number_to_find = input().split() #яких метеликів ми хочемо перевірити

dictionary = {}
for number in numbers:
    if number in dictionary:
        dictionary[number] += 1
    else:
        dictionary[number] = 1

for what_need_to_find in number_to_find:
    if what_need_to_find in dictionary:
        print("YES")
    else:
        print("NO")