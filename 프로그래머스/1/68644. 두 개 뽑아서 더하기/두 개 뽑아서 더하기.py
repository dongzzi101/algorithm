def solution(numbers):
    answer = []
    nums = []
    
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            nums.append(numbers[i] + numbers[j])
    
    
    nums = list(set(nums))
    nums.sort()
    answer = nums
            
    return answer