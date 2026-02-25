TC = int(input())

for _ in range(TC):
	N, M = map(int, input().split())
	
	arrA = list(map(int, input().split()))
	arrB = list(map(int, input().split()))

	arrA.sort()
	arrB.sort()

	main = 0
	sub = 0
	count = 0

	while main < N:
		if sub == M:
			count += sub
			main += 1
		else:
			if arrA[main] > arrB[sub]:
				sub += 1
			else:
				count += sub
				main += 1

	print(count)
	
