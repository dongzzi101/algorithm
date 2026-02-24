
K = int(input())

stack = []

for i in range(K):
	num = int(input())

	if num == 0:
		stack.pop(-1)
	else:
		stack.append(num)


sum = 0
for e in stack:
	sum += e

print(sum)