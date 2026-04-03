N, M = map(int, input().split())

bulbs = [0] + list(map(int, input().split()))

for _ in range(M):
	a, b, c = map(int, input().split())

	if a == 1:
		bulbs[b] = c
	
	elif a == 2:
		for i in range(b, c+1):
			if bulbs[i] == 0:
				bulbs[i] = 1
			else:
				bulbs[i] = 0
	
	elif a == 3:
		for i in range(b, c+1):
			bulbs[i] = 0
		
	elif a == 4:
		for i in range(b, c+1):
			bulbs[i] = 1

print(*bulbs[1:])