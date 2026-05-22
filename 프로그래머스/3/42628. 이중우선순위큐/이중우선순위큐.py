import heapq

def solution(operations):
    heap = []
    
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        
        if command == 'I':
            heapq.heappush(heap, num)
        
        elif command == 'D':
            
            if not heap:
                continue
            
            if num == -1:
                heapq.heappop(heap)
                
            elif num == 1:
                max_val = max(heap)
                heap.remove(max_val)
                heapq.heapify(heap)
    
    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), heap[0]]
    
