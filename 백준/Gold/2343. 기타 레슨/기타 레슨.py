N, M = map(int, input().split())

time = list(map(int,input().split()))

left = max(time)
right = sum(time)

answer = 0
while left <= right:
	middle = (left + right) // 2

	blueray_num = 1
	remain = middle

	for i in range(N):
		if remain < time[i]:
			blueray_num += 1
			remain = middle

		remain -= time[i]

	if blueray_num <= M:
		answer = middle
		right = middle - 1
	else:
		left = middle + 1


print(answer)

	