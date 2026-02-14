from collections import deque

def solution(n, computers):
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited, n)
            count += 1
            
    return count


def bfs(start, computers, visited, n):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        node = q.popleft()
        
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
