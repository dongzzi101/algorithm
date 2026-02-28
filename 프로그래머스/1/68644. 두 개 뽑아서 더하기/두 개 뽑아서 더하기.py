from itertools import combinations

def solution(numbers):
    answer = []
    s = set()
    
    for i in combinations(numbers, 2):
        s.add(sum(i))
    
    
    answer = list(sorted(s))
    return answer