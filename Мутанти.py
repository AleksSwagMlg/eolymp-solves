n = input() #кількість звіряток (0 ≤ n ≤ 10^5)
colors = input().split() #кольори
m = input() #кількість запитів  (1 ≤ m ≤ 100000)
colors_to_find = input().split() #які кольори ми хочемо перевірити

dictionary = {}
for color in colors:
    if color in dictionary:
        dictionary[color] += 1
    else:
        dictionary[color] = 1

for what_need_to_find in colors_to_find:
    if what_need_to_find in dictionary:
        print(dictionary[what_need_to_find])
    else:
        print(0)