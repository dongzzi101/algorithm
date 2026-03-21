def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse = True)
    
    result = 0
    for i in range(len(A)):
        result += (A[i] * B[i])
    
    answer = result
    return answer