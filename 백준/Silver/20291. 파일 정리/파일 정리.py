N = int(input())

extends_map = {}
for _ in range(N):
	name, extend = input().split(".")

	if extend in extends_map:
		extends_map[extend] += 1
	else:
		extends_map[extend] = 1


for i in sorted(extends_map):
	print(i, extends_map[i])
