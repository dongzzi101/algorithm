import sys

board = [list(map(int, input().split())) for _ in range(5)]
checked = [[0] * 5 for _ in range(5)]

count = 0
for _ in range(5):
    call = list(map(int, input().split()))
    for num in call:
        count += 1

        for i in range(5):
            for j in range(5):
                if board[i][j] == num:
                    checked[i][j] = 1

        line = 0

        for i in range(5):
            if sum(checked[i]) == 5:
                line += 1

        for j in range(5):
            s = 0
            for i in range(5):
                s += checked[i][j]
            if s == 5:
                line += 1

        if checked[0][0] + checked[1][1] + checked[2][2] + checked[3][3] + checked[4][4] == 5:
            line += 1

        if checked[0][4] + checked[1][3] + checked[2][2] + checked[3][1] + checked[4][0] == 5:
            line += 1

        if line >= 3:
            print(count)
            sys.exit()
