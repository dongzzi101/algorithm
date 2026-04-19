def solution(ingredient):
    count = 0
    stack = []
    
    for ingre in ingredient:
        stack.append(ingre)
        
        if len(stack) >= 4:
            if stack[-4:] == [1, 2, 3, 1]:
                for _ in range(4):
                    stack.pop()
                count += 1
    
    return count