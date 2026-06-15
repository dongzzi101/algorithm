def solution(skill, skill_trees):
    answer = 0
    
    
    for skill_tree in skill_trees:
        remain_skill = []
        
        for st in skill_tree:
            if st not in skill:
                continue
            remain_skill.append(st)
        
        if "".join(remain_skill) == skill[:len(remain_skill)]:
            answer += 1
    
    return answer