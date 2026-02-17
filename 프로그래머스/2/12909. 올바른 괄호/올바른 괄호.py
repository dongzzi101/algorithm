def solution(s):
    stack = []

    for i in range(len(s)):
        if s[0] == ")":
            return False

        if s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True
