def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]     
        new_arr = array[i-1:j]
        new_arr.sort()
        answer.append(new_arr[k-1])
    
    return answer