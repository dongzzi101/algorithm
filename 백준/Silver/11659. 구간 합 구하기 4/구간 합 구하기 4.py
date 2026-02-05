import sys
input = sys.stdin.readline

def get_sum(a, b):
    return parr[b] - parr[a - 1]


N, M = map(int, input().split())
arr = list(map(int, input().split()))

parr = [0] * (N + 1)

for i in range(1, N + 1):
    parr[i] = parr[i - 1] + arr[i - 1]

for _ in range(M):
    a, b = map(int, input().split())
    print(get_sum(a, b))
