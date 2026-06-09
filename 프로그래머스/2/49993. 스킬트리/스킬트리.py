def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        temp = []
        for sk in skill_tree:
            if sk in skill:
                temp.append(sk)
        
        extracted_skill = "".join(temp)
        
        if extracted_skill == skill[:len(temp)]:
            answer += 1
    
    
    return answer