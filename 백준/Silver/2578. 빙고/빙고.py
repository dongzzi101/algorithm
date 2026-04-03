bingo_pan = [list(map(int, input().split())) for _ in range(5)]

call_number = []

for _ in range(5):
	call_number += list(map(int, input().split()))


def change_num_in_bingo_pan(num):
	for y in range(5):
		for x in range(5):
			if bingo_pan[y][x] == num:
				bingo_pan[y][x] = 0

def check_count_bingo():
    count = 0

    # 가로
    for y in range(5):
        if all(bingo_pan[y][x] == 0 for x in range(5)):
            count += 1

    # 세로
    for x in range(5):
        if all(bingo_pan[y][x] == 0 for y in range(5)):
            count += 1

    # 대각선
    if all(bingo_pan[i][i] == 0 for i in range(5)):
        count += 1

    if all(bingo_pan[i][4-i] == 0 for i in range(5)):
        count += 1

    return count

	
		

call_count = 0
bingo_count = 3

for num in call_number:
    call_count += 1
    change_num_in_bingo_pan(num)
    
    if check_count_bingo() >= 3:
        print(call_count)
        break
