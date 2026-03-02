import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()

def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

def upper_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left

for _ in range(M):
    start, end = map(int, input().split())

    left_idx = lower_bound(dots, start)
    right_idx = upper_bound(dots, end)

    print(right_idx - left_idx)