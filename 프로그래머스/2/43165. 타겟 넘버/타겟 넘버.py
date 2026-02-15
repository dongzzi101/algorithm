def dfs(numbers, target, depth, current_sum):
    if depth == len(numbers):
        if current_sum == target:
            return 1
        else:
            return 0

    return (
        dfs(numbers, target, depth + 1, current_sum + numbers[depth]) +
        dfs(numbers, target, depth + 1, current_sum - numbers[depth])
    )


def solution(numbers, target):
    return dfs(numbers, target, 0, 0)
