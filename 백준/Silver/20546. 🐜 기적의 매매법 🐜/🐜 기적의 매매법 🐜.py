import sys

money = int(input())
stock_prices = list(map(int, input().split()))

def bnp(money, stock_prices):
    quantity = 0

    for day in range(14):
        if money >= stock_prices[day]:
            bought = money // stock_prices[day]
            quantity += bought
            money -= bought * stock_prices[day]

    return (quantity * stock_prices[-1]) + money

def timing(money, stock_prices):
    quantity = 0
    up_count = 0
    down_count = 0

    for day in range(1, 14):
        if stock_prices[day] > stock_prices[day - 1]:
            up_count += 1
            down_count = 0
        elif stock_prices[day] < stock_prices[day - 1]:
            down_count += 1
            up_count = 0
        else:
            up_count = 0
            down_count = 0

        if down_count == 3:
            bought = money // stock_prices[day]
            quantity += bought
            money -= bought * stock_prices[day]

        elif up_count == 3:
            money += quantity * stock_prices[day]
            quantity = 0

    return (quantity * stock_prices[-1]) + money


bnp_result = bnp(money, stock_prices)
timing_result = timing(money, stock_prices)

if bnp_result > timing_result:
    print("BNP")
elif bnp_result < timing_result:
    print("TIMING")
else:
    print("SAMESAME")
