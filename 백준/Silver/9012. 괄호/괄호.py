n = int(input())

for _ in range(n):
    s = input().strip()
    stack = []
    valid = True

    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                valid = False
                break
            stack.pop()

    if valid and not stack:
        print("YES")
    else:
        print("NO")

