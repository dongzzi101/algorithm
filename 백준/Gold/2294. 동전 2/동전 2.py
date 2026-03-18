N, K = map(int, input().split())

coins = set()

for _ in range(N):
	coins.add(int(input()))

INF = K+1
dp = [INF] * (K+1)

dp[0] = 0

for coin in coins:
	for j in range(1, K+1):
		if j-coin >= 0:
			dp[j] = min(dp[j], dp[j-coin]+1)

print(-1 if dp[K] == INF else dp[K])
