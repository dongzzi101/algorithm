def solution(arr):
    answer = []
    n = len(arr)
    
    if n == 1:
        return [-1]
    else:
        min_value = min(arr)
        arr.remove(min_value)
        return arr
    
