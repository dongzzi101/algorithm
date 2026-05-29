from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    
    padding_storage = []
    padding_storage.append(['.'] * (m + 2))

    for row in storage:
        padding_storage.append(['.'] + list(row) + ['.'])

    padding_storage.append(['.'] * (m + 2))
    
    max_y = n + 2
    max_x = m + 2
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    def only_container(target_char):
        visited = [[False] * max_x for _ in range(max_y)]
        
        q = deque([(0, 0)])
        visited[0][0] = True
        
        targets = set() 
        
        while q:
            y, x = q.popleft()
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if 0 <= ny < max_y and 0 <= nx < max_x and not visited[ny][nx]:
                    if padding_storage[ny][nx] == '.':
                        visited[ny][nx] = True
                        q.append((ny, nx))
                    elif padding_storage[ny][nx] == target_char:
                        visited[ny][nx] = True
                        targets.add((ny, nx))
        
        for y, x in targets:
            padding_storage[y][x] = '.'
            
    def use_crane(target_char):
        for y in range(max_y):
            for x in range(max_x):
                if padding_storage[y][x] == target_char:
                    padding_storage[y][x] = '.'

    for req in requests:
        if len(req) == 1:
            only_container(req)
        else:
            use_crane(req[0]) 
            
    answer = 0
    for y in range(max_y):
        for x in range(max_x):
            if padding_storage[y][x] != '.': 
                answer += 1
                
    return answer