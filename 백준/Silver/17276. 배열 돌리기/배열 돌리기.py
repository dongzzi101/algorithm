T = int(input())


def rotate_45(arr, n):
    mid = n // 2
    new = [row[:] for row in arr]

    for i in range(n):
        new[i][mid] = arr[i][i]
        new[i][n - 1 - i] = arr[i][mid]
        new[mid][n - 1 - i] = arr[i][n - 1 - i]
        new[i][i] = arr[mid][i]

    return new


for _ in range(T):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    k = (d // 45) % 8

    for _ in range(k):
        arr = rotate_45(arr, n)

    for row in arr:
        print(*row)

