n = int(input())

INF = 1e9
dp = [INF] * (n+1)

dp[0] = 0

for i in range(3, n+1):
    if i - 3 >= 0:
        dp[i] = min(dp[i], dp[i-3] + 1)
    if i - 5 >= 0:
        dp[i] = min(dp[i], dp[i-5] + 1)

print(dp[n] if dp[n] != INF else -1)