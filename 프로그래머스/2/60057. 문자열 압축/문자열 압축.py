def solution(s):
    n = len(s)

    if n == 1:
        return 1

    answer = n

    for step in range(1, (n // 2) + 1):
        prev = s[0:step]
        count = 1
        compressed = ""

        for i in range(step, n, step):
            cur = s[i:i+step]

            if cur == prev:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev

                prev = cur
                count = 1

        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev

        answer = min(answer, len(compressed))

    return answer