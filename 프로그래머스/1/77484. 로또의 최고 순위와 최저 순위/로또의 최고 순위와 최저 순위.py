def solution(lottos, win_nums):
    zero_count = 0
    
    for lotto in lottos:
        if lotto == 0:
            zero_count += 1
    
    count = 0
    for win_num in win_nums:
        if win_num in lottos:
            count += 1
    
    max_winning = count + zero_count
    min_winning = count
    
    rank = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6
    }
    
    
    return [rank[max_winning], rank[min_winning] ]