from itertools import combinations

def solution(number):
    answer = 0
    count = 0
    for i in list(combinations(number, 3)):
        if sum(i) == 0:
            count += 1
    
    answer = count
    return answer