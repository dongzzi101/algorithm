N, K = map(int, input().split())
S1 = list(map(int, input().split()))
D = list(map(int, input().split()))

result = [0] * N
visited = [False] * N

for i in range(N):
    if visited[i]:
        continue

    cycle = []
    cur = i
    while not visited[cur]:
        visited[cur] = True
        cycle.append(cur)
        cur = D[cur] - 1

    L = len(cycle)

    for idx in range(L):
        result[cycle[(idx + K) % L]] = S1[cycle[idx]]

print(*result)
