def solution(num_list):
    gob = 1
    hob = 0
    for num in num_list:
        gob *= num
        hob += num
    
    if (hob * hob) > gob:
        return 1
    else:
        return 0
