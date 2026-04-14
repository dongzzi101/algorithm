from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    orders = [''.join(sorted(order)) for order in orders]
    
    for k in course:
        comb_list = []
        
        for order in orders:
            comb_list += combinations(order, k)
        
        counter = Counter(comb_list)
        
        if not counter:
            continue
        
        max_count = max(counter.values())
        
        if max_count < 2:
            continue
        
        for comb in counter:
            if counter[comb] == max_count:
                answer.append(''.join(comb))
    
    return sorted(answer)