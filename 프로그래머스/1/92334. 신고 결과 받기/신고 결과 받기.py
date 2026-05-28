def solution(id_list, report, k):
    report_map = {}
    
    for r in report:
        user_id, reported_user = r.split()
        
        if reported_user in report_map:
            report_map[reported_user].add(user_id)
        else:
            report_map[reported_user] = {user_id}
    
    mail_count = {user: 0 for user in id_list}
    
    for reported_user, senders in report_map.items():
        if len(senders) >= k:
            for sender in senders:
                mail_count[sender] += 1
    
    result = []
    
    for user in id_list:
        result.append(mail_count[user])
    
    return result