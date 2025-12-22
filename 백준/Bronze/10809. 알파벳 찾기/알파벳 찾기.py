word = input()

alphabet = [-1] * 26

for i in range(len(word)):
    idx = ord(word[i]) - ord('a')

    if alphabet[idx] == -1:
        alphabet[idx] = i

print(*alphabet)


