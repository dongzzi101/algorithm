s = input()

result = ""
temp = ""
inside_tag = False

for ch in s:
    if ch == '<':
        result += temp[::-1]
        temp = ""
        inside_tag = True
        result += ch

    elif ch == '>':
        inside_tag = False
        result += ch

    elif ch == ' ':
        if inside_tag:
            result += ch
        else:
            result += temp[::-1] + ' '
            temp = ""

    else:
        if inside_tag:
            result += ch
        else:
            temp += ch

result += temp[::-1]

print(result)