
def bfs(sy, sx, ey, ex):
	q = []
	v = [0] * N

	q.append((sy, sx))

	while q:
		cy, cx = q.pop(0)

		if abs(cy -ey) + abs(cx -ex) <= 1000:
			return "happy"

		for i in range(N):
			if v[i] == 0:
				ny, nx = lst[i]
				if abs(cy -ny) + abs(cx -nx) <= 1000:
					 q.append((ny, nx))
					 v[i] = 1

	return "sad"


tc = int(input())

for _ in range(tc):
	N = int(input())
	sy, sx = map(int, input().split())
	lst = []
	for _ in range(N):
		ty, tx = map(int, input().split())
		lst.append((ty, tx))
	ey, ex = map(int, input().split())

	ans = bfs(sy, sx, ey, ex)
	print(ans)