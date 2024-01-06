line = input()
line = line.replace("!", "0").replace("?", "0").replace(".", "0")

array = line.split("0")

sentens = 0
for word in array:
    if word != "":
        sentens += 1

print(sentens)