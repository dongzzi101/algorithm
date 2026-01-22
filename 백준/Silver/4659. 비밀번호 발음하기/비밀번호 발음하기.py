vowels = ['a', 'e', 'i', 'o', 'u']
while True:
    password = input()

    if password == 'end':
        break

    has_vowel = False
    vowel_cnt = 0
    cons_cnt = 0
    prev = ''
    acceptable = True

    for ch in password:
        if ch in vowels:
            has_vowel = True
            vowel_cnt += 1
            cons_cnt = 0
        else:
            cons_cnt += 1
            vowel_cnt = 0

        if vowel_cnt == 3 or cons_cnt == 3:
            acceptable = False
            break

        if prev == ch and ch not in ['e', 'o']:
            acceptable = False
            break

        prev = ch

    if not has_vowel:
        acceptable = False

    if acceptable:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")




