import sys

n = int(input())

result = []

for _ in range(n):
    nn = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    print(nums[0], nums[-1])
