def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        filtered = ""

        for ch in skill_tree:
            if ch in skill:
                filtered += ch
        
        if skill.startswith(filtered):
            answer += 1
    
    return answer