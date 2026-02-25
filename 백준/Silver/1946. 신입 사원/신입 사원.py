import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
	num = int(input())

	candidates = []

	for _ in range(num):
		paper, interview = map(int, input().split())
		candidates.append((paper, interview))

	candidates.sort()

	top_ranking = 1e9
	count  = 0
	for i in range(num):
		if candidates[i][1] < top_ranking:
			count +=1
			top_ranking = candidates[i][1]
	
	print(count)

