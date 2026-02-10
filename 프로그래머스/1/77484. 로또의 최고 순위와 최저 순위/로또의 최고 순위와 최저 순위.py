def solution(lottos, win_nums):
    answer = []
    count = 0
    zero_count = 0

    for num in win_nums:
        if num in lottos:
            count += 1

    for lotto in lottos:
        if lotto == 0:
            zero_count += 1

    best_count = count + zero_count
    worst_count = count

    def rank(n):
        if n == 6:
            return 1
        elif n == 5:
            return 2
        elif n == 4:
            return 3
        elif n == 3:
            return 4
        elif n == 2:
            return 5
        else:
            return 6

    answer.append(rank(best_count))
    answer.append(rank(worst_count))

    return answer
