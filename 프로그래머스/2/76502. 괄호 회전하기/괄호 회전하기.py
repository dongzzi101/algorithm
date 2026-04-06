def solution(s):
    answer = 0
    
    def is_valid(s):
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return 0
                
                top = stack.pop()
                if pairs[ch] != top:
                    return 0
        
        return 1 if not stack else 0
    
    for _ in range(len(s)):
        answer += is_valid(s)
        s = s[1:] + s[0]
    
    return answer