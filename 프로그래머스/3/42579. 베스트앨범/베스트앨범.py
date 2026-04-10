def solution(genres, plays):
    answer = []
    
    genres_map = {}
    play_map = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in genres_map:
            genres_map[genre] = []
            play_map[genre] = 0
        
        genres_map[genre].append((i, play))
        play_map[genre] += play
    
    sorted_items = sorted(play_map.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in sorted_items:
        sorted_songs = sorted(genres_map[genre], key=lambda x : (-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])
    
    return answer