N = int(input())

cards =[0] + list(map(int, input().split()))
coins = [ i for i in range(0, N+2)]


dp = [0] * (N+1)
dp[1] = cards[1]


for i in range(1, N+1):
	for j in range(1, N+1):
		if j - i >= 0:
			dp[j] = max(dp[j], dp[j-i] + cards[i])

print(dp[N])