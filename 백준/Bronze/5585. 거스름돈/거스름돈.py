cost = int(input())

pay = 1000

ret_money =  pay - cost

count = 0

coin500 = ret_money // 500
ret_money %= 500

coin100 = ret_money // 100
ret_money %= 100

coin50 = ret_money // 50
ret_money %= 50

coin10 = ret_money // 10
ret_money %= 10

coin5 = ret_money // 5
ret_money %= 5

coin1 = ret_money // 1
ret_money %= 1


count = coin500 + coin100 + coin50 + coin10 + coin5 + coin1
print(count)