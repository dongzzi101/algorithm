from collections import deque

TC = int(input())

for _ in range(TC):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    q = deque()
    for i in range(N):
        q.append((i, priorities[i]))

    printed = 0

    while q:
        idx, p = q.popleft()

        if any(p2 > p for _, p2 in q):
            q.append((idx, p))
        else:
            printed += 1
            if idx == M:
                print(printed)
                break
