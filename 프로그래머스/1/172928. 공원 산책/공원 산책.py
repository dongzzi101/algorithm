def solution(park, routes):
    answer = []
    
    height = len(park)
    width = len(park[0])
    
    def find_start_pos():
        for y in range(height):
            for x in range(width):
                if park[y][x] == 'S':
                    return y, x
    
    move = {
        'N' : (-1, 0),
        'S' : (1, 0),
        'W' : (0, -1),
        'E' : (0, 1)
    }
    
    cur_y, cur_x = find_start_pos()
    
    for route in routes:
        direction, command = route.split()
        distance = int(command)
        
        temp_y, temp_x = cur_y, cur_x
        is_possible = True
        
        for _ in range(distance):
            temp_y += move[direction][0]
            temp_x += move[direction][1]
        
            if not (0 <= temp_y < height and 0 <= temp_x < width) or park[temp_y][temp_x] == 'X':
                    is_possible = False
                    break
        
        if is_possible:
            cur_y, cur_x = temp_y, temp_x
            
    return [cur_y, cur_x]