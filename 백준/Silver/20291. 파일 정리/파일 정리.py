N = int(input())

extends_map = {}

for _ in range(N):
	name, extends = input().split(".")

	if extends in extends_map:
		extends_map[extends] += 1
	else:
		extends_map[extends] = 1




for i in sorted(extends_map):
	print(i, extends_map[i])
