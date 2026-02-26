from queue import PriorityQueue

N = int(input())

arr = list(int(input()) for _ in range(N))

pq = PriorityQueue()

for i in range(1, N):
	pq.put(-arr[i])

if N == 1:
	print(0)
else:
	count = 0
	while True:
		max_value = -pq.get()
		if max_value < arr[0]:
			break

		max_value -= 1
		arr[0] += 1
		count += 1
		pq.put(-max_value)

	print(count)



