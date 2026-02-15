from collections import deque

def solution(arr):
    q = deque()
    q.append(arr[0])
    
    for x in arr[1:]:
        if q[-1] != x:
            q.append(x)

    return list(q)