N, K = map(int, input().split())
temp = list(map(int, input().split()))

prefix = [0 for _ in range(N + 1)]

for i in range(N):
    prefix[i + 1] = prefix[i] + temp[i]

answer = []
for k in range(K, N + 1):
    answer.append(prefix[k] - prefix[k - K])

print(max(answer))
