def solution(clothes):
    clothes_map = {}
    
    for name, kind in clothes:
        if kind in clothes_map:
            clothes_map[kind] += 1
        else:
            clothes_map[kind] = 1
    
    answer = 1
    for count in clothes_map.values():
        answer *= (count + 1)
    
    return answer - 1