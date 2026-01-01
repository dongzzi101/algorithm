N = int(input())

arr = list(map(int, input().split()))


arr.sort()

total = 0

for i in range(N):
    for j in range(i+1):
        total += arr[j]

print(total)


