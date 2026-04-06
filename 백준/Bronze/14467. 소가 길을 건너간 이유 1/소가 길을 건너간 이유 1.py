N = int(input())

cow_map = {}
count = 0

for _ in range(N):
	cow_number, pos = map(int, input().split())

	if cow_number in cow_map:
		if cow_map[cow_number] != pos:
			count += 1

	cow_map[cow_number] = pos

print(count)

