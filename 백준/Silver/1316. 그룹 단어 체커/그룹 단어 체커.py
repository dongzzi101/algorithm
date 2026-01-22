N = int(input())
count = 0

for _ in range(N):
    word = input()

    exist = []
    prev = ''
    ok = True

    for ch in word:
        if ch != prev:
            if ch in exist:
                ok = False
                break
            exist.append(ch)
        prev = ch

    if ok:
        count += 1

print(count)
