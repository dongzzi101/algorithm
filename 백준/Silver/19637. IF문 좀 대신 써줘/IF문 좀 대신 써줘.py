import sys
input = sys.stdin.readline

N, M = map(int, input().split())

titles = []
levels = []

for _ in range(N):
	title, level = input().split()
	titles.append(title)
	levels.append(int(level))



for _ in range(M):
	value = int(input())

	left = 0
	right = N -1

	while left <= right:
		mid = (left + right) // 2

		if value <= levels[mid]:
			right = mid - 1
		else:
			left = mid + 1

	print(titles[left])

	
