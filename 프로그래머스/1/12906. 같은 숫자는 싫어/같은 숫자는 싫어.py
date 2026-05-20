def solution(arr):
    answer = []
    
    n = len(arr)
    
    temp = arr[0]
    answer.append(temp)
    for i in range(1, n):
        if arr[i] == temp:
            continue
        temp = arr[i]
        answer.append(temp)

    return answer