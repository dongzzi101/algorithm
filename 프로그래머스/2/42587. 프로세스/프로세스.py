from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    while q:
        first = q.popleft()
        
        if any(first[0] < item[0] for item in q):
            q.append(first)
        else:
            answer += 1
            if first[1] == location:
                return answer

    return answer