def solution(nums):
    num_set = set(nums)
    
    if len(num_set) <= (len(nums) / 2):
        return len(num_set)
    else:
        return len(nums) / 2
    
