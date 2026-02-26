N = int(input())
M = int(input())

adjs = [[] for _ in range(N)]


for _ in range(M):
	a, b = map(int, input().split())
	adjs[a-1].append(b-1)
	adjs[b-1].append(a-1)

friend = [0] * N

for i in adjs[0]:
	friend[i] = 1

friend2 = [0] * N

for i in range(N):
	if friend[i] == 0:
		continue

	for j in adjs[i]:
		if j != 0 and friend[j] == 0:
			friend2[j] = 1

print(sum(friend) + sum(friend2))