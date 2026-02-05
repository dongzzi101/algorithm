import sys
input = sys.stdin.readline

def get_sum(sy, sx, ey, ex):
	global parr
	return parr[ey][ex] - (parr[ey][sx - 1] + parr[sy - 1][ex] - parr[sy - 1][sx - 1])

N, M = map(int, input().split())

arr = [[0] * (N + 1)]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

parr = [ [0] * (N+1) for _ in range(N+1)]

for n in range(1, N + 1):
	for m in range(1, N + 1):
		parr[n][m] = (parr[n - 1][m] + parr[n][m - 1] - parr[n - 1][m - 1]) + arr[n][m]

for _ in range(M):
	sy, sx, ey, ex = map(int, input().split())
	print(get_sum(sy, sx, ey, ex))
