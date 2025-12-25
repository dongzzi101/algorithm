s = input().rstrip()

result = []
temp = []
inside_tag = False

for ch in s:
    if ch == "<":
        if temp:
            result.extend(reversed(temp))
            temp.clear()
        inside_tag = True
        result.append(ch)

    elif ch == ">":
        inside_tag = False
        result.append(ch)

    elif inside_tag:
        result.append(ch)

    else:
        if ch == " ":
            result.extend(reversed(temp))
            temp.clear()
            result.append(" ")
        else:
            temp.append(ch)

if temp:
    result.extend(reversed(temp))

print("".join(result))
