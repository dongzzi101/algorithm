def solution(sizes):
    answer = 0

    w = []
    h = []

    for size in sizes:
        bigger = max(size)
        smaller = min(size)

        w.append(bigger)
        h.append(smaller)
    
    answer = max(w) * max(h)


    return answer