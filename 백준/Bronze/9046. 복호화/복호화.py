T = int(input())
for _ in range(T):
    s = input().strip()

    count = [0] * 26

    for ch in s:
        if 'a' <= ch <= 'z':
            count[ord(ch) - ord('a')] += 1

    max_count = max(count)

    if count.count(max_count) > 1:
        print('?')
    else:
        idx = count.index(max_count)
        print(chr(idx + ord('a')))
