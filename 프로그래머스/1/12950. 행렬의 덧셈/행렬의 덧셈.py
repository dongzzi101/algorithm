def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    
    answer = [[0] * m for _ in range(n)]
    
    for y in range(n):
        for x in range(m):
            answer[y][x] = arr1[y][x] + arr2[y][x]
    
    return answer