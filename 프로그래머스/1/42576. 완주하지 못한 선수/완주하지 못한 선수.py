def solution(participant, completion):
    answer = ''
    
    paricipant_map = {}
    
    for p in participant:
        if p in paricipant_map:
            paricipant_map[p] += 1
        else:
            paricipant_map[p] = 1
    
    for c in completion:
        if c in paricipant_map:
            paricipant_map[c] -= 1
    
    for name, count in paricipant_map.items():
        if count != 0:
            return name
        
    return answer