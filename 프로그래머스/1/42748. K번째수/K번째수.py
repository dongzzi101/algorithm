def solution(array, commands):
    answer = []
    
    for command in commands:
        start, end, target = command
        new_arr = array[start-1 : end]
        new_arr.sort()
        answer.append(new_arr[target-1])
    
    return answer