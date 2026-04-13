import heapq

def solution(book_time):
    
    def to_min(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    book_time.sort(key=lambda x: x[0])
    
    heap = []  
    
    for start, end in book_time:
        start = to_min(start)
        end = to_min(end) + 10 
        
        if heap and heap[0] <= start:
            heapq.heappop(heap) 
        
        heapq.heappush(heap, end)  
    
    return len(heap)