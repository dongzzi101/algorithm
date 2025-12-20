word = input()

n = int(input())

count = 0
for ch in word:
    count += 1
    if count == n:
        print(ch)
