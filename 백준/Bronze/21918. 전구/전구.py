import sys

n, m = map(int, input().split())
lights = [0] + list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        lights[b] = c

    elif a == 2:
        for i in range(b, c + 1):
            lights[i] = 1 - lights[i]

    elif a == 3:
        for i in range(b, c + 1):
            lights[i] = 0

    elif a == 4:
        for i in range(b, c + 1):
            lights[i] = 1

print(' '.join(map(str, lights[1:])))
