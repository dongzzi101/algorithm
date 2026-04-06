N = int(input())
switches = list(map(int, input().split()))

students = int(input())

for _ in range(students):
    gender, target = map(int, input().split())

    if gender == 1:
        for i in range(target, N + 1, target):
            switches[i - 1] = 1 - switches[i - 1]

    else:
        idx = target - 1
        switches[idx] = 1 - switches[idx]

        left = idx - 1
        right = idx + 1

        while left >= 0 and right < N and switches[left] == switches[right]:
            switches[left] = 1 - switches[left]
            switches[right] = 1 - switches[right]
            left -= 1
            right += 1

for i in range(N):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()