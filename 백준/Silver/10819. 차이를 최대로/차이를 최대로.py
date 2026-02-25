from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

max_diff_sum = -10

result = 0
for lis in permutations(arr, N):
	diff_sum = 0
	for i in range(N-1):
		diff_sum += abs(lis[i] - lis[i+1])

	max_diff_sum = max(diff_sum, max_diff_sum)

print(max_diff_sum)




