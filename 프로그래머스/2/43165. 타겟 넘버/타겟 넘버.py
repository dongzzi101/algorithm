def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
    
    
        add_case = dfs(index + 1, current_sum + numbers[index])
        sub_case = dfs(index + 1, current_sum - numbers[index])
    
        return add_case + sub_case
    
    return dfs(0,0)
