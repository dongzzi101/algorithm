from collections import deque

N = int(input())
moves = list(map(int, input().split()))

q = deque((i + 1, moves[i]) for i in range(N))
answer = []

while q:
    idx, k = q.popleft()
    answer.append(idx)

    if not q:
        break

    if k > 0:
        q.rotate(-(k - 1))
    else:
        q.rotate(-k)

print(*answer)
