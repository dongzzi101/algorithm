n = int(input())

answer = 0

if n % 4 == 0:
    if n % 100 != 0:
        answer = 1
    elif n % 400 == 0:
        answer = 1
    else:
        answer = 0
else:
    answer = 0

print(answer)