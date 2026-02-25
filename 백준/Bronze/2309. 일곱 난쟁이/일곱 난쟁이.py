from itertools import combinations

kids = []

for _ in range(9):
	kids.append(int(input()))

kids.sort()
target = sum(kids) - 100

i = 0
while True:
	a, b = list(combinations(kids, 2))[i]

	if (a + b) == target:
		break
	i += 1

kids.remove(a)
kids.remove(b)

for kid in kids:
    print(kid)


