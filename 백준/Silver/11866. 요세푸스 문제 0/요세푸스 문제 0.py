from collections import deque

N, K = map(int, input().split())

arr = deque(range(1, N + 1))
result = []

while arr:
    for _ in range(K - 1):
        arr.append(arr.popleft())

    result.append(arr.popleft())

print("<" + ", ".join(map(str, result)) + ">")
