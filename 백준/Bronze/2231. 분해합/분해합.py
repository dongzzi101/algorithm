N = int(input())

answer = 0

for i in range(1, N + 1):
    s = i
    temp = i

    while temp > 0:
        s += temp % 10
        temp //= 10

    if s == N:
        answer = i
        break

print(answer)
