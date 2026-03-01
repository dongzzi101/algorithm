def solution(s):
    answer = ""
    
    word_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    word = ""
    for ch in s:
        if ch.isdigit():
            answer += ch
        else:
            word += ch
            if word in word_map:
                answer += word_map[word]
                word = ""
    
    return int(answer)