def solution(diffs, times, limit):
    
    def calc_time(level):
        total = 0
        
        for i in range(len(diffs)):
            diff = diffs[i]
            time = times[i]
            
            if diff <= level:
                total += time
            else:
                fail = diff - level
                prev_time = times[i-1]
                total += fail * (time + prev_time) + time
            
            if total > limit:
                return total
        
        return total
    
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if calc_time(mid) <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer