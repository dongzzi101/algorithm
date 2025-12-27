isbn = list(input())

total = 0
pos = 0
for i in range(len(isbn)):
    if isbn[i] == '*':
        pos = i
        continue

    num = int(isbn[i])

    if (i + 1) % 2 == 0:
        total += num * 3
    else:
        total += num

if (pos + 1) % 2 == 0:
    weight = 3
else:
    weight = 1

for x in range(10):
    if (total + weight * x) % 10 == 0:
        print(x)
        break
