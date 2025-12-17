n = int(input())

bulbs = list(map(int, input().split()))

students = int(input())

for _ in range(students):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number - 1, n, number):
            bulbs[i] = 1 - bulbs[i]


    else:
        center = number - 1
        left = center - 1
        right = center + 1
        while left >= 0 and right < n and bulbs[left] == bulbs[right]:
            left -= 1
            right += 1

        for i in range(left + 1, right):
            bulbs[i] = 1 - bulbs[i]

for i in range(0, n, 20):
    print(*bulbs[i:i+20])