import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

total = sum(nums)

print(round(total / N))

print(nums[N // 2])

cnt = Counter(nums)
max_freq = max(cnt.values())

modes = [k for k, v in cnt.items() if v == max_freq]
modes.sort()

print(modes[0] if len(modes) == 1 else modes[1])
print(nums[-1] - nums[0])
