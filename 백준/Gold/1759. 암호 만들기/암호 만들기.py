
L, C  = map(int, input().split())
arr = input().split()
vows = ['a', 'e', 'i', 'o', 'u']

arr.sort()

choose = []

def is_possible():
	global L, C, choose, arr

	vow = 0
	for i in choose:
		vow += (i in vows)
	con = L - vow

	return (vow >= 1 and con >= 2)

def comb(index, level):
	global L, C, choose, arr
	 

	if level == L:
		if is_possible():
			print(''.join(choose))
		return

	for i in range(index, C):
		choose.append(arr[i])
		comb(i + 1, level + 1)
		choose.pop()

comb(0,0)
