def convert_time(time):
    in, out = time.split(",")
    convert_number(in)
    convert_number(out)


def convert_number(time):
    hh, mm = time.split(":")
    print(hh)
    print(mm)
    
    
    


def solution(book_time):
    answer = 0
    
    book_time.sort(key=lambda x : x[0])
    for b in book_time:
        convert_time(b)
    
    print(book_time)
    
    
    
    return answer