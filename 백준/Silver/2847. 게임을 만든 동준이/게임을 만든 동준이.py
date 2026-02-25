N = int(input())

level = [int(input()) for _ in range(N)]

count = 0

for i in range(N-2, -1, -1):
	if level[i] >= level[i+1]:
		count += level[i] - (level[i+1] -1)
		level[i] = level[i+1] - 1

print(count)
		
	



