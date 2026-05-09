def solution(s):
    nums = list(map(int, s.split()))
    max_num = max(nums)
    min_num = min(nums)
    return f"{min_num} {max_num}"