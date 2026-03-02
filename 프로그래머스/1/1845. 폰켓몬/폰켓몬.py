def solution(nums):
    answer = 0
    s = set()
    nums.sort()
    
    for i in range(len(nums)):
        s.add(nums[i])
    
    if len(s) <= len(nums) // 2:
        return len(s)
    else:
        return len(nums) // 2
    
    return answer