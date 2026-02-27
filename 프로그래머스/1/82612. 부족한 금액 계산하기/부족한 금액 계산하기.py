def solution(price, money, count):
    total_spend = 0
    
    for i in range(count):
        total_spend += (price * (i +1) )
    
    total_cost = total_spend - money

    if total_cost >= 0:
        return total_cost
    else:
        return 0
