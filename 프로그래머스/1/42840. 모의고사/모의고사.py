def solution(answers):
    answer = []
    
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    student1_answer_count = 0
    student2_answer_count = 0
    student3_answer_count = 0
    
    scores = [] 
    
    for i in range(len(answers)):
        if answers[i] == student1[i % len(student1)]:
            student1_answer_count += 1
        
        if answers[i] == student2[i % len(student2)]:
            student2_answer_count += 1
        
        if answers[i] == student3[i % len(student3)]:
            student3_answer_count += 1
    
    scores.append(student1_answer_count)
    scores.append(student2_answer_count)
    scores.append(student3_answer_count)
    
    max_score = max(scores)
    highest_score = []
    
    for i, score in enumerate(scores):
        if score == max_score:
            highest_score.append(i+1)
    
    return highest_score