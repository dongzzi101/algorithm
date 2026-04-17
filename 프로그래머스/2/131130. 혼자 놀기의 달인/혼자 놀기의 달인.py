def solution(cards):
    visited = [False] * (len(cards) + 1)
    sizes = []
    
    sizes = []
    
    def dfs(start):
        cur = start
        cnt = 0
        
        while not visited[cur]:
            visited[cur] = True
            cur = cards[cur - 1]
            cnt += 1
        
        return cnt

    for i in range(1, len(cards) + 1):
        if not visited[i]:
            sizes.append(dfs(i))
    
    sizes.sort(reverse=True)

    if len(sizes) < 2:
        return 0

    return sizes[0] * sizes[1]