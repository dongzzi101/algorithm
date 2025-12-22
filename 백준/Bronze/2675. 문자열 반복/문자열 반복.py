
T = int(input())

for _ in range(T):
    N, T = input().split()

    answer = []
    for _ in T:
        answer.append(_ * int(N))

    print(*answer, sep='')