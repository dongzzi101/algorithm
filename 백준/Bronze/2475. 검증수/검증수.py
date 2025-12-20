nums = list(map(int, input().split()))

result = 0
for num in nums:
    result += num * num

answer = result % 10
print(answer)