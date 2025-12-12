import sys

n = int(input())

pos = [-1] * 11
count = 0

for i in range(n):
    num, direction = map(int, input().split())

    if pos[num] == -1:
        pos[num] = direction
        continue

    if pos[num] != direction:
        count += 1
        pos[num] = direction

print(count)
