from collections import deque

def solution(queue1, queue2):
    main_que, sub_que = deque(queue1), deque(queue2)
    
    total = sum(main_que + sub_que)
    if total % 2 == 1:
        return -1
    target = total // 2
    
    main_sum = sum(main_que)
    
    count = 0
    limit = len(queue1) * 3 
    
    while count <= limit:
        if main_sum == target:
            return count
        
        elif main_sum < target:
            value = sub_que.popleft()
            main_sum += value
            main_que.append(value)
            count += 1
        elif main_sum > target:
            value = main_que.popleft()
            main_sum -= value
            sub_que.append(value)
            count += 1
        
    return -1
            