def solution(n):
    answer = 0
    
    num_list = list(map(int, str(n)))
    num_list.sort(reverse=True)
    
    answer = int("".join(map(str, num_list)))
    

    return answer