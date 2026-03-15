n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    best = 0

    for j in range(i):
        if arr[i] < arr[j]:
            best = max(best, dp[j])

    dp[i] = best + 1

print(max(dp))