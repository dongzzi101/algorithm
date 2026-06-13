def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])

    answer = [[0] * col for _ in range(row)]
    
    for y in range(row):
        for x in range(col):
            answer[y][x] = arr1[y][x] + arr2[y][x]
    
    return answer