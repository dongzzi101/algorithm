from collections import deque

def solution(s):
    q = deque(s)
    count = 0
    n = len(s)
    
    pair = {')': '(', ']': '[', '}': '{'}
    
    for _ in range(n):
        stack = []
        valid = True
        
        for ch in q:
            if ch in pair:
                if stack and stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    valid = False
                    break
            else:
                stack.append(ch)
        
        if valid and not stack:
            count += 1
        
        q.append(q.popleft())
    
    return count