def solution(answers):
    # patterns = [
    #     [1, 2, 3, 4, 5],
    #     [2, 1, 2, 3, 2, 4, 2, 5],
    #     [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # ]
    
    answer = []
    
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    supo1_answer_count = 0
    supo2_answer_count = 0
    supo3_answer_count = 0
    
    
    for i in range(len(answers)):
        if answers[i] == supo1[i % len(supo1)]:
            supo1_answer_count += 1
            
    for i in range(len(answers)):
        if answers[i] == supo2[i % len(supo2)]:
            supo2_answer_count += 1
            
    for i in range(len(answers)):
        if answers[i] == supo3[i % len(supo3)]:
            supo3_answer_count += 1
    
    result = []
    
    result.append(supo1_answer_count)
    result.append(supo2_answer_count)
    result.append(supo3_answer_count)
    
    max_score = max(result)
    
    for i in range(len(result)):
        if result[i] == max_score:
            answer.append(i+1)
    
    answer.sort()
    
    return answer