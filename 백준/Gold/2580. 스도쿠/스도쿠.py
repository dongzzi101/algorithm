def is_possible(y, x, n):
	global board

	for col in range(9):
		if board[y][col] == n:
			return False

	for row in range(9):
		if board[row][x] == n:
			return False

	for row in range(3):
		for col in range(3):
			if board[3 * (y // 3) + row][3 * (x // 3) + col] == n:
				return False

	return True


def search(lev):
	global board, pos

	if lev == len(pos):
		for i in range(9):
			for j in range(9):
				print(board[i][j], end=' ')
			print()
		exit(0)
		return

	y, x = pos[lev]

	for n in range(1, 10):
		if is_possible(y, x, n):
			board[y][x] = n
			search(lev + 1)
			board[y][x] = 0



board = [list(map(int, input().split())) for _ in range(9)]


pos = []

for i in range(9):
	for j in range(9):
		cur = board[i][j]
		if cur == 0:
			pos.append((i, j))

search(0)




