def solution(targets):
    targets.sort(key=lambda x : x[1])

    shot = -1
    count = 0

    for s, e in targets:
        if s >= shot:
            count += 1
            shot = e
    
    return count