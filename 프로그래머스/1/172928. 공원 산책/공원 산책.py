def solution(park, routes):
    dir_maps = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    
    H = len(park)
    W = len(park[0])
    
    current_y, current_x = 0, 0
    for y in range(H):
        for x in range(W):
            if park[y][x] == "S":
                current_y, current_x = y, x
                break
                
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        dy, dx = dir_maps[op]
        
        ny, nx = current_y, current_x
        is_possible = True
        
        for _ in range(n):
            ny += dy
            nx += dx
            
            if not (0 <= ny < H and 0 <= nx < W) or park[ny][nx] == "X":
                is_possible = False
                break
        
        if is_possible:
            current_y, current_x = ny, nx
            
    return [current_y, current_x]