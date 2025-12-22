N = int(input())

for _ in range(N):
    result = input()

    score = 0
    in_row = 0

    for ch in result:
        if ch == "O":
            in_row += 1
            score += in_row
        else:
            in_row = 0

    print(score)
