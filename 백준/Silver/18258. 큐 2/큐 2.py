import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
output = []

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push":
        q.append(command[1])

    elif command[0] == "front":
        output.append(q[0] if q else -1)

    elif command[0] == "back":
        output.append(q[-1] if q else -1)

    elif command[0] == "size":
        output.append(len(q))

    elif command[0] == "empty":
        output.append(0 if q else 1)

    elif command[0] == "pop":
        output.append(q.popleft() if q else -1)

sys.stdout.write("\n".join(map(str, output)))
