from collections import deque

def solution(food):
    answer = ''
    q = deque()
    
    for i in range(len(food)):
        count = food[i] // 2
        
        if count >= 1:
            while count > 0:
                q.append(str(i))
                count -= 1        

    
    opposite = deque(reversed(q))
    return ''.join(q) + '0' + ''.join(opposite)