def solution(my_string):
    answer = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for ch in my_string:
        if ch in vowels:
            continue
        answer += ch
    
    return answer