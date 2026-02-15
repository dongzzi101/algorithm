def solution(id_list, report, k):
    st = set()
    
    for r in report:
        a, b = r.split()
        st.add((a, b))
    
    count = {name : 0 for name in id_list}
    report_set = {name : set() for name in id_list}
    
    for name1, name2 in st:
        report_set[name1].add(name2)
        count[name2] += 1
    
    answer = []
    for name in id_list:
        mail_count = 0
        for n in report_set[name]:
             if count[n] >= k:
                mail_count += 1
        answer.append(mail_count)
    
    return answer