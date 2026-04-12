from collections import deque

def solution(order):
    answer = 0
    
    main_container = [i+1 for i in range(len(order))]
    main_container = deque(main_container)
    
    sub_container = []

    count = 0
    idx = 0
    
    while main_container:
        if main_container[0] == order[idx]:
            main_container.popleft()
            count += 1
            idx += 1
        else:
            sub_container.append(main_container.popleft())
        
        while sub_container and sub_container[-1] == order[idx]:
            sub_container.pop()
            count += 1
            idx += 1
    
    answer = count    
    return answer