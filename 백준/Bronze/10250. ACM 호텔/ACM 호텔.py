T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        floor = H
        unit = N // H
    else:
        floor = N % H
        unit = N // H + 1

    print(f"{floor}{unit:02d}")
