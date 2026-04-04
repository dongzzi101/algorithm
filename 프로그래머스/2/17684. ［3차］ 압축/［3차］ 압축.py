def solution(msg):
    answer = []
    dict_map = {}
    
    for i in range(26):
        dict_map[chr(ord('A') + i)] = i + 1
    
    i = 0
    while i < len(msg):
        
        j = i + 1
        while j <= len(msg) and msg[i:j] in dict_map:
            j += 1

        w = msg[i:j-1]  
        answer.append(dict_map[w])
        
        if j <= len(msg):
            dict_map[msg[i:j]] = len(dict_map) + 1

        i += len(w)
            
    return answer