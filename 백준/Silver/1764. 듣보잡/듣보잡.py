n, m = map(int, input().split())

nobody = {}

for _ in range(n+m):
	name = input()

	if name in nobody:
		nobody[name] += 1
	else:
		nobody[name] = 1

result = []

for name in nobody:
    if nobody[name] > 1:
        result.append(name)

result.sort()

print(len(result))

for name in result:
    print(name)
