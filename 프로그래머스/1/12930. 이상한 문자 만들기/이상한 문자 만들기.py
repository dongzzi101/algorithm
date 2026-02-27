def solution(s):
    answer = ""
    index = 0
    
    for ch in s:
        if ch == " ":
            answer += ch
            index = 0
        else:
            if index % 2 == 0:
                answer += ch.upper()
            else:
                answer += ch.lower()
            index += 1
    
    return answer