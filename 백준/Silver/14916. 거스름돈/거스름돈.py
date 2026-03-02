N = int(input())

result = -1

for coin5 in range(N // 5, -1, -1):
	remain = N - (coin5 * 5)

	if remain % 2 == 0:
		coin2 = remain // 2
		result = coin5 + coin2
		break

print(result)
