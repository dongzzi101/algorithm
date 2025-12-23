stack = []

first_num = int(input())

count = first_num
while count >= 1:
    first_num = int(input())

    if first_num == 0:
        stack.pop()
        count -= 1
    else:
        stack.append(first_num)
        count -= 1

print(sum(stack))
