def solution(s):
    words_index = [-1] * len(s)
    words_map = {}
    
    for idx, ch in enumerate(s):
        if ch in words_map:
            words_index[idx] = idx - words_map[ch]
            words_map[ch] = idx
        else:
            words_map[ch] = idx
            
    
    return words_index