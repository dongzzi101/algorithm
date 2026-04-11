from collections import Counter

def solution(topping):
    right_counter = Counter(topping)
    left_set = set()
    
    count = 0
    
    for t in topping:
        left_set.add(t)

        right_counter[t] -= 1
        if right_counter[t] == 0:
            del right_counter[t]

        if len(left_set) == len(right_counter):
            count += 1
    
    return count