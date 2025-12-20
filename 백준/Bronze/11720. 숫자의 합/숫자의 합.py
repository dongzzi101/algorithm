N = int(input())
nums = input()

arr = []

for num in nums:
    arr.append(num)

answer = 0
for i in arr:
    answer += int(i)

print(answer)
