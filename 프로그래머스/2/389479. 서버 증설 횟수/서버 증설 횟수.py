def solution(players, m, k):
    answer = 0
    active_servers = 0
    
    added_servers = [0] * 24
    
    for i in range(24):
        
        if i >= k:
            active_servers -= added_servers[i-k]
        
        needed_servers = players[i] // m
        
        if active_servers < needed_servers:
            num_to_add = needed_servers - active_servers
            
            answer += num_to_add
            active_servers += num_to_add
            added_servers[i] = num_to_add
    
    return answer