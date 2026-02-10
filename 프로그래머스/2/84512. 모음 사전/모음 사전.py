def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0

    for a in vowels:
        count += 1
        if a == word:
            return count

        for b in vowels:
            ab = a + b
            count += 1
            if ab == word:
                return count

            for c in vowels:
                abc = ab + c
                count += 1
                if abc == word:
                    return count

                for d in vowels:
                    abcd = abc + d
                    count += 1
                    if abcd == word:
                        return count

                    for e in vowels:
                        abcde = abcd + e
                        count += 1
                        if abcde == word:
                            return count

