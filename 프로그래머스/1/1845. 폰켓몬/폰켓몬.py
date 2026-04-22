def solution(nums):
    max_get = len(nums) // 2
    nums = list(set(nums))
    
    if max_get <= len(nums):
        return max_get
    else:
        return len(nums)
    
    
