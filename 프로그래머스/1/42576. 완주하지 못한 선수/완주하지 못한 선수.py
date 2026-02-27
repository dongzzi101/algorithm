def solution(participant, completion):
    d = {}
    
    for p in participant:
        d[p] = d.get(p, 0) + 1
    
    for c in completion:
        d[c] -= 1
    
    for name, count in d.items():
        if count > 0:
            return name
    
