def solution(players, callings):
    
    players_map = {player: i for i, player in enumerate(players)}
    
    def find_player_then_change(target):
        current_index = players_map[target]
        front_index = current_index - 1
        front_player = players[front_index]
        
        players[current_index], players[front_index] = players[front_index], players[current_index]
        
        players_map[target] = front_index
        players_map[front_player] = current_index
        
    
    for calling in callings:
        find_player_then_change(calling)
        
    return players