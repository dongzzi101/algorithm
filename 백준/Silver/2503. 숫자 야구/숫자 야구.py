import sys

n = int(input())
hint = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):

            if a == b or b == c or c == a:
                continue

            candidate = [a, b, c]
            valid = True

            for number, strike, ball in hint:
                num = [
                    number // 100,
                    (number // 10) % 10,
                    number % 10
                ]

                ball_count = 0
                strike_count = 0

                for i in range(3):
                    if candidate[i] == num[i]:
                        strike_count += 1
                    elif candidate[i] in num:
                        ball_count += 1

                if strike_count != strike or ball_count != ball:
                    valid = False
                    break

            if valid:
                answer += 1

print(answer)
