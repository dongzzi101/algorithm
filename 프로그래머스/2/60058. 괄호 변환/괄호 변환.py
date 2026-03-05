from collections import deque

def is_correct_parenthesis(string):
    stack = []

    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


def change_to_correct_parenthesis(balanced_parentheses_string):
    if balanced_parentheses_string == '':
        return ''

    u, v = separate_u_v(balanced_parentheses_string)

    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])


def reverse_parenthesis(string):
    reversed_string = ""

    for c in string:
        if c == '(':
            reversed_string += ')'
        elif c == ')':
            reversed_string += '('

    return reversed_string


def separate_u_v(string):
    queue = deque(string)
    left_count, right_count = 0, 0
    u, v = "", ""

    while queue:
        ch = queue.popleft()
        u += ch

        if ch == "(":
            left_count += 1
        if ch == ")":
            right_count += 1

        if left_count == right_count:
            break

    v = ''.join(queue)

    return u, v


def solution(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)