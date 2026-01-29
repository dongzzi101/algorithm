def solution(elements):
    n = len(elements)
    arr = elements + elements
    answer = set()
    
    for length in range(1, n+1):
        for start in range(n):
            answer.add(sum(arr[start:start+length]))
    
    return len(answer)