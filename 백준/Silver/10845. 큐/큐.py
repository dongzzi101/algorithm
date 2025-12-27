import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()
result = []

for _ in range(N):
    command = input().split()

    if command[0] == "push":
        q.append(command[1])

    elif command[0] == "pop":
        result.append(q.popleft() if q else "-1")

    elif command[0] == "size":
        result.append(str(len(q)))

    elif command[0] == "empty":
        result.append("0" if q else "1")

    elif command[0] == "front":
        result.append(q[0] if q else "-1")

    elif command[0] == "back":
        result.append(q[-1] if q else "-1")

print("\n".join(result))
