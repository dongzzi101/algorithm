N = int(input())

num = 1
for i in range(1, N + 1):
    num *= i

cnt = 0
while num % 10 == 0:
    cnt += 1
    num //= 10

print(cnt)
