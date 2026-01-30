def is_valid(t):
    stack=[]
    match = {')' : '(',']' : '[','}' : '{'}
    
    for ch in t:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack[-1] != match[ch]:
                return False
            stack.pop()
    
    return len(stack) == 0
        
def solution(s):
    n = len(s)
    arr = s+s
    answer = 0
    
    for i in range(n):
        
        t = arr[i:i+n]
        
        if is_valid(t):
            answer += 1
    
    return answer