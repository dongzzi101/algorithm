def solution(name, yearning, photo):
    answer = []
    yearning_map = {}
    
    for i in range(len(name)):
        yearning_map[name[i]] = yearning[i]
    
    score = 0
    for y in range(len(photo)):
        for x in range(len(photo[y])):
            if photo[y][x] in yearning_map:
                score += yearning_map[photo[y][x]]
        
        answer.append(score)
        score = 0
    
    return answer