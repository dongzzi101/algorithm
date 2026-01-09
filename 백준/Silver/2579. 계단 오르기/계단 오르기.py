stairs = int(input())
arr = [int(input()) for _ in range(stairs)]

dp = [[-1e9] * 3 for _ in range(stairs)]

dp[0][1] = arr[0]

if stairs > 1:
    dp[1][1] = arr[1]
    dp[1][2] = arr[0] + arr[1]

for i in range(2, stairs):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]

print(max(dp[stairs-1][1], dp[stairs-1][2]))
