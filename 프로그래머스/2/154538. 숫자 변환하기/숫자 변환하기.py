from collections import deque

def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    visited = set()
    
    while q:
        cur, count = q.popleft()
        
        if cur == y:
            return count
        
        for next in [cur + n, cur * 2, cur * 3]:
            if next <= y and next not in visited:
                visited.add(next)
                q.append((next, count + 1))
    
    return -1