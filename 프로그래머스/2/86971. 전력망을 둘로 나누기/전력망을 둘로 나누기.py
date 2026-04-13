def solution(n, wires):
    answer = n
    
    adjs = [[] for _ in range(n+1)]
    
    for a, b in wires:
        adjs[a].append(b)
        adjs[b].append(a)
    
    def dfs(node, visited, cut_a, cut_b):
        visited[node] = True
        count = 1
        
        for next in adjs[node]:
            if (node == cut_a and next == cut_b) or (node == cut_b and next == cut_a):
                continue
            
            if not visited[next]:
                count += dfs(next, visited, cut_a, cut_b)
        
        return count
    
    for a, b in wires:
        visited = [False] * (n+1)
        size = dfs(1, visited, a, b)
        
        diff = abs(size - (n - size))
        answer = min(answer, diff)
    
    return answer