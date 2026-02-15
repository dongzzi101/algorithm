def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    answer = []

    def dfs(curr, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return True   
        
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == curr:
                visited[i] = True
                if dfs(tickets[i][1], path + [tickets[i][1]]):
                    return True
                visited[i] = False
        
        return False

    dfs("ICN", ["ICN"])
    return answer[0]
