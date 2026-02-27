def get_sum(x):
    return sum(map(int, str(x)))    

def solution(x):
    answer = False
    answer = x % get_sum(x) == 0
    return answer