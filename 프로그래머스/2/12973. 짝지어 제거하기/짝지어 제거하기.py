def solution(s):
    answer = 0
    
    stack = []
    
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    
    
    return 1 if len(stack) == 0 else 0