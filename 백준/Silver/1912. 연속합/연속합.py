N = int(input())

arr = [0] + list(map(int, input().split()))

dp = [0] * (N+1)


if max(arr[1:]) < 0:
	print(max(arr[1:]))

else:
	for i in range(1, N+1):
		dp[i] = max(dp[i-1] + arr[i], 0)

	print(max(dp))