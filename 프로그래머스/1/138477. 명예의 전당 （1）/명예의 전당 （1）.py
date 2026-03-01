def solution(k, score):
    answer = []
    top_k_list = []
    
    for cur_score in score:
        
        if len(top_k_list) < k:
            top_k_list.append(cur_score)
            
        else:
            if cur_score > min(top_k_list):
                top_k_list.remove(min(top_k_list))
                top_k_list.append(cur_score)
        
        answer.append(min(top_k_list))
        
    return answer