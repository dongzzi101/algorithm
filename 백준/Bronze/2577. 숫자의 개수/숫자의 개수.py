result = 1
for _ in range(3):
    result *= int(input())

arr = [0] * 10

for ch in str(result):
    arr[int(ch)] += 1

for count in arr:
    print(count)
