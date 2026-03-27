N, K = map(int, input().split())

coins = []
for _ in range(N):
	coins.append(int(input()))

coins.sort(reverse=True)

count = 0

for i in range(len(coins)):
	if coins[i] > K:
		continue
	else:
		use = K // coins[i]
		count += use
		K -= (coins[i] * use)

	if K == 0:
		break

print(count)


