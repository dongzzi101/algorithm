N = int(input())
arr = list(map(int, input().split()))

arr.sort()

s = 0
result = 0
for a in arr:
	s += a
	result += s

print(result)