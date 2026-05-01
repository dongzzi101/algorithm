def solution(participant, completion):
    answer = ''
    
    participant_dict = {}
    
    for p in participant:
        if p in participant_dict:
            participant_dict[p] += 1
        else:
            participant_dict[p] = 0
    
    for c in completion:
        participant_dict[c] -= 1
    
    for pd in participant_dict:
        if participant_dict[pd] >= 0:
            answer = pd
                
    return answer