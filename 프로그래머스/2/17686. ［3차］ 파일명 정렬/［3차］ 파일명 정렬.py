def solution(files):

    def split_file(file):
        head, number, tail = "", "", ""

        i = 0

        while i < len(file) and not file[i].isdigit():
            head += file[i]
            i += 1

        while i < len(file) and file[i].isdigit():
            number += file[i]
            i += 1

        tail = file[i:]
        
        return head, number, tail
    
    parsed = []

    for file in files:
        head, number, tail = split_file(file)
        parsed.append((head, number, tail, file))
    
    parsed.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    answer = []

    for x in parsed:
        answer.append(x[3])

    return answer
