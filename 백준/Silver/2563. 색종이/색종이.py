N = int(input())


arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
	y, x = map(int, input().split())

	for i in range(y, y+10):
		for j in range(x, x+10):
			arr[i][j] = 1


ans = 0
for row in arr:
	ans += sum(row)

print(ans)
