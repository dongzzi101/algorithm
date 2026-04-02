def solution(record):
    user_map = {}
    
    for user_info in record:
        parts = user_info.split()
        
        if parts[0] in ["Enter", "Change"]:
            uid = parts[1]
            nickname = parts[2]
            user_map[uid] = nickname
    
    logs = []
    for user_info in record:
        parts = user_info.split()

        if parts[0] == "Enter":
            logs.append((parts[1], "in"))
        elif parts[0] == "Leave":
            logs.append((parts[1], "out"))
    
    answer = []
    for uid, action in logs:
        if action == "in":
            answer.append(f"{user_map[uid]}님이 들어왔습니다.")
        else:
            answer.append(f"{user_map[uid]}님이 나갔습니다.")
    
    return answer