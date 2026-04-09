from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    want_dic = {name: number[i] for i, name in enumerate(want)}
    window = defaultdict(int)
    
    for i in range(10):
        window[discount[i]] += 1
    
    def is_valid():
        for key in want_dic:
            if window[key] != want_dic[key]:
                return False
        return True
    
    if is_valid():
        answer += 1
    
    for i in range(10, len(discount)):
        window[discount[i-10]] -= 1
        window[discount[i]] += 1
        
        if is_valid():
            answer += 1
    
    return answer