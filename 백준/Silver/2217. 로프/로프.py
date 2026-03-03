N = int(input())

weights = []

for _ in range(N):
	weights.append(int(input()))

weights.sort()

answer = 0

for i in range(N):
	answer = max(answer, weights[i] * (N - i))

print(answer)
