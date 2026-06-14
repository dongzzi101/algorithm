def solution(n, lost, reserve):
    answer = 0
    
    students = [i+1 for i in range(n)]
    
    students_map = {}
    
    for student in students:
        students_map[student] = 0
    
    for lost_student in lost:
        students_map[lost_student] -= 1
    
    for reserve_student in reserve:
        students_map[reserve_student] += 1
    
    
    for sm in students_map:
        if students_map[sm] < 0:
            if sm - 1 in students_map and students_map[sm - 1] > 0:
                students_map[sm] += 1
                students_map[sm - 1] -= 1
            elif sm + 1 in students_map and students_map[sm + 1] > 0:
                students_map[sm] += 1
                students_map[sm + 1] -= 1
        
    for sm in students_map:
        if students_map[sm] >= 0:
            answer += 1
        
    return answer