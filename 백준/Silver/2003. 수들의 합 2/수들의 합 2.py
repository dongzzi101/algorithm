N, M = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
right = 0

sum = arr[0]

count = 0

while True:
	if sum == M:
		count += 1

	if sum >= M:
		left += 1
		sum -= arr[left-1]
	
	else:
		if right == N - 1:
			break
		
		right += 1
		sum += arr[right]
		

print(count)