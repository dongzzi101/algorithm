N, M = map(int, input().split())
parent = list(map(int, input().split()))

for i in range(1, N):
	parent[i] -= 1

prize = [0] * N
for i in range(M):
	id, score = list(map(int, input().split()))
	prize[id - 1] += score

total_prize = [0] * N
for i in range(1, N):
	total_prize[i] = total_prize[parent[i]] + prize[i]

print(*total_prize)

