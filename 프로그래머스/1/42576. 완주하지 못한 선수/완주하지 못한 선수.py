def solution(participant, completion):
    answer = ''
    
    participants_map = {}
    
    for p in participant:
        if p in participants_map:
            participants_map[p] += 1
        else:
            participants_map[p] = 0
    
    for c in completion:
        if c in participants_map:
            participants_map[c] -= 1
    
    for key, value in participants_map.items():
        if value == 0:
            answer += key
    
    return answer