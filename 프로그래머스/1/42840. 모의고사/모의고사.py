def solution(answers):
    answer = []
    n = len(answers)
    
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    supo1_count = 0
    supo2_count = 0
    supo3_count = 0

    for i in range(len(answers)):
        if supo1[i % len(supo1)] == answers[i]:
            supo1_count += 1

        if supo2[i % len(supo2)] == answers[i]:
            supo2_count += 1

        if supo3[i % len(supo3)] == answers[i]:
            supo3_count += 1
    
    scores =[supo1_count, supo2_count, supo3_count]
    max_score = max(scores)

    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)

    return answer