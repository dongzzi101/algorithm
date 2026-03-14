n = int(input())

count = 0

for _ in range(n):
    letter = [0] * 26
    word = input()
    prev = ''

    is_group = True

    for ch in word:
        idx = ord(ch) - ord('a')

        if ch != prev:
            if letter[idx]:
                is_group = False
                break
            letter[idx] = 1

        prev = ch

    if is_group:
        count += 1

print(count)