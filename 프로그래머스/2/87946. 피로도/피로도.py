def dfs(k, count):
    global answer, visited

    answer = max(answer, count)

    for i in range(n):
        if not visited[i]:
            need, cost = dungeons[i]
            if k >= need:
                visited[i] = True
                dfs(k - cost, count + 1)
                visited[i] = False  


def solution(k, dungeons_input):
    global n, dungeons, visited, answer

    dungeons = dungeons_input
    n = len(dungeons)
    visited = [False] * n
    answer = 0

    dfs(k, 0)
    return answer
