from collections import deque

def solution(players, m, k):
    server_upgrade_count = 0
    
    servers = deque()  
    
    for i, player in enumerate(players):
        while servers and servers[0] <= i:
            servers.popleft()
        
        need = player // m
        
        current = len(servers)
        
        if need > current:
            add = need - current
            server_upgrade_count += add
            
            for _ in range(add):
                servers.append(i + k)
    
    return server_upgrade_count