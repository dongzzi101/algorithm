str1 = input()
str2 = input()
str3 = input()

arr = [str1, str2, str3]

next_num = 0

for i in range(len(arr)):
    if arr[i].isdigit():
        num = int(arr[i])
        next_num = num + (3 - i)
        break

if next_num % 15 == 0:
    print("FizzBuzz")
elif next_num % 5 == 0:
    print("Buzz")
elif next_num % 3 == 0:
    print("Fizz")
else:
    print(next_num)
