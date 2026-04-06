def solution(dirs):
    commands = {
        "U": (1, 0),
        "D": (-1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }
    
    cur_y, cur_x = 0, 0
    visited = set()
    
    for dir in dirs:
        dy, dx = commands[dir]
        
        ny = cur_y + dy
        nx = cur_x + dx
        
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            
            if (cur_y, cur_x, ny, nx) not in visited:
                visited.add((cur_y, cur_x, ny, nx))
                visited.add((ny, nx, cur_y, cur_x))
            
            cur_y, cur_x = ny, nx
    
    return len(visited) // 2