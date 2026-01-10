import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

freq = {}
for x in cards:
    freq[x] = freq.get(x, 0) + 1

M = int(input())
targets = list(map(int, input().split()))

result = []

for x in targets:
    count = freq.get(x, 0)
    result.append(str(count))

print(' '.join(result))