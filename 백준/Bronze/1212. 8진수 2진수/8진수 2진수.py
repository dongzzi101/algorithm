import sys

s = str(input())
digits = list(map(int, s))

result = []
for digit in digits:
    a = digit // 4
    b = (digit % 4) // 2
    c = digit % 2

    result += str(a) + str(b) + str(c)

answer = ''.join(result)
s = answer.lstrip('0')

if s == "":
    print("0")
else:
    print(s)
