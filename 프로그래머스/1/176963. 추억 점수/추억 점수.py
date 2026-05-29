def solution(name, yearning, photo):
    answer = []
    
    yearning_map = {}
    
    for i in range(len(name)):
        if name[i] in yearning_map:
            yearning_map[name[i]] += 0
        else:
            yearning_map[name[i]] = yearning[i]
    
    
    
    for y in range(len(photo)):
        result = 0
        for x in range(len(photo[y])):
            if photo[y][x] in yearning_map:
                result += yearning_map[photo[y][x]]
        
        answer.append(result)
    
    return answer