N = int(input())

arr = [ i for i in range(1, N+1)]


check = [False] * N
choose = []


def permutatation(level):
	if level == N:
		print(*choose)
		return


	for i in range(0, N):
		if check[i] == True:
			continue

		choose.append(arr[i])
		check[i] = True

		permutatation(level+1)

		check[i] = False
		choose.pop()

permutatation(0)




