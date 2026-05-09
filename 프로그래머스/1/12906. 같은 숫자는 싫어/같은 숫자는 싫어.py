def solution(arr):
    answer = []
    before = arr[0]
    answer.append(arr[0])
    
    for idx, num in enumerate(arr):
        if idx > 0:
            if before == arr[idx]:
                continue
            else:
                answer.append(num)
        
        before = arr[idx]
        
    return answer