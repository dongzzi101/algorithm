def solution(dirs):
    answer = set()
    
    def is_valid(ny, nx):
        return (-5 <= ny <= 5) and (-5 <= nx <= 5)
    
    def update_location(y, x, dir):
        if dir == "U":
            ny, nx = y+1, x
        elif dir == "D":
            ny, nx = y-1, x
        elif dir == "L":
            ny, nx = y, x-1
        elif dir == "R":
            ny, nx = y, x+1
        
        return ny, nx
    
    
    y, x = 0, 0 
    
    for dir in dirs:
        ny, nx = update_location(y, x, dir)
        if is_valid(ny, nx):
            answer.add((y, x, ny, nx))
            answer.add((ny, nx, y, x))
            y, x = ny, nx
    
    return len(answer) // 2