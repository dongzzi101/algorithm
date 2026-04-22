def solution(n):
    nums = list(str(n))
    nums.sort(reverse=True)
    result = ''.join(nums)
    return int(result)